import hashlib
import json
import os
import re

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Data:

    def process_browser_log_entry(self, entry):
      response = json.loads(entry['message'])['message']
      return response

    def parse_url(self, url):

      request_protocol = re.match("^[http|file]+s?", url).group(0)

      url_id = hashlib.md5(bytes(url, 'utf-8')).hexdigest()

      if re.match("^http.*", url) is not None:
        
        domain = re.match(r'^([a-z]+[\.|a-z|]+)',url.replace(request_protocol + '://', '')).group(0)
        
        request_path = url.replace(request_protocol + '://','').replace(domain, '')[1:]
        
      elif re.match("^file.*", url) is not None:
        
        domain = 'file'
        
        request_path = url.replace(request_protocol + '://','')[1:]

      return {
        'url_id': url_id,
        'request_protocol': request_protocol,
        'domain': domain,
        'request_path': request_path
         }


    def __init__(self):

        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}


        chrome_options = Options()
        chrome_options.add_argument("no-sandbox")
        chrome_options.add_argument("headless")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("window-size=1900,1080");

        driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)

        self.urls = []
        self.suffux_path = os.path.realpath('./build')
        self.urls += [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser('./build')) for f in fn if f.endswith('.html')]


        data = {
          'page_load_resource_links': {}, 
          'source_files': [], 
          'hyperlinks': {} 
        }


        for check_file in self.urls:
        
            check_url = 'file://' + self.suffux_path + check_file.replace('./build','')
            source_file = check_file.replace('./build','')[1:]

            if source_file not in data['source_files']:
              data['source_files'].append(source_file)

            driver.get(check_url)

            links =  driver.find_elements_by_css_selector("a")

            for link in links:

              link_location = link.location

              url = link.get_attribute('href')

              link = self.parse_url(url)

              hyperlink_source_file = {'name': source_file, 'location': link_location}

              if link['url_id'] in data['hyperlinks']:

                data['hyperlinks'][link['url_id']]['source_files'].append(hyperlink_source_file)

              else:

                link['source_files'] = [ hyperlink_source_file ]
                data['hyperlinks'][link['url_id']] = link


            events = [self.process_browser_log_entry(entry) for entry in driver.get_log('performance')]

            for entry in events:

                if entry['method'] == 'Network.requestWillBeSent':

                  http_status = str([response['params']['response']['status'] for response in events if response['method'] == 'Network.responseReceived' and response['params']['requestId'] == entry['params']['requestId']]).replace('[', '').replace(']', '')

                  url = str(entry['params']['request']['url'])


                  url_id = hashlib.md5(bytes(url, 'utf-8')).hexdigest()


                  if re.match("^http|file.*", url) is not None:

                    source_file_line_number = ''

                    if 'lineNumber' in entry['params']['initiator']:

                      source_file_line_number = str(entry['params']['initiator']['lineNumber'])

                    request_protocol = re.match("^[http|file]+s?", url).group(0)

                    if re.match("^http.*", url) is not None:

                      domain = re.match(r'^([a-z]+[\.|a-z|]+)',url.replace(request_protocol + '://', '')).group(0)

                      request_path = url.replace(request_protocol + '://','').replace(domain, '')[1:]

                      
                    elif re.match("^file.*", url) is not None:

                      domain = 'file'

                      request_path = url.replace(request_protocol + '://','')[1:]

                    if url_id in data['page_load_resource_links']:

                      data['page_load_resource_links'][url_id]['source_files'].append({'name': source_file, 'line_number': source_file_line_number, 'http_status': http_status})
                      
                    else:

                      data['page_load_resource_links'][url_id] = {'url': url, 'request_protocol': request_protocol, 'domain': domain, 'request_path': request_path, 'source_files': [ {'name': source_file, 'line_number': source_file_line_number, 'http_status': http_status} ]}

        driver.close()
        self.test_data = data


print("\n"+'Creating test data')
print("\n\ntest data:\n" + json.dumps(Data().test_data, indent=2, default=str))

