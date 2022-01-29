import pytest
import os

from conftest import Data

class Test:

    data = Data()

    def setup_class(self):
        #copy data so it can be used
        self.source_files = self.data.test_data['source_files']


    def setup_method(self):
        pass


    @pytest.mark.parametrize(
        argnames='data', 
        argvalues=[link for url_id, link in data.test_data['hyperlinks'].items() if link['request_protocol'][0:4] =='http'], 
        ids=[url_id for url_id, link in data.test_data['hyperlinks'].items() if link['request_protocol'][0:4] =='http']
    )
    def test_hyperlink_external_alive_check(self, data):
        """Test hyperlinks that are found within each page of the site.

        SSL verification has been disabled as this test only checks if the link is alive and valid.

        Args:
            data (dict): A dictionary of hyperlinks constructed within conftest.py
        """
        from requests import get
        from requests import packages
        from urllib3.exceptions import InsecureRequestWarning

        packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        request = get(data['url'], verify=False)

        print(str(data) + str(request.status_code))

        assert request.status_code == 200, (
            f"Hyperlink [{data['url_id']}] to location [{data['url']}] failed," 
            f"with status [{request.status_code}].")


    @pytest.mark.parametrize(
        argnames='data',
        argvalues=[link for url_id, link in data.test_data['hyperlinks'].items() if link['request_protocol'][0:4] =='file' and link['request_path'] != ''],
        ids=[url_id for url_id, link in data.test_data['hyperlinks'].items() if link['request_protocol'][0:4] =='file' and link['request_path'] != '']
    )
    def test_hyperlink_internal_alive_check(self, data):
        """ Test all internal hyperlinks are valid and the page exists.

        This test constructs the actual file path from a found internal (contains file as the protocol) link. After the link is found it is checked against the pages that exist.

        Args:
            data (list): list of dictionaries containing the urls to test
        """

        path_suffix = os.path.realpath('./build')

        print('URL Data:' + str(data))

        request_path = str(data['request_path'])

        if request_path[0:1] == '/':
            if request_path[0:1] == request_path:
                request_path = 'index.html'
            else:
                request_path = request_path[1:]

        if '#' in request_path:
            request_path_split = request_path.split('#')
            request_path = str(request_path_split[0])
            print('Debug # in path ' + request_path_split[0])

        # Reconstruct a valid url. append 'index.html' for paths ending in '/'
        if (request_path[len(request_path)-1:] == '/'
            and request_path[len(request_path)-5:] != '.html'
        ):

            request_path = str(request_path) + 'index.html'

        elif (request_path[len(request_path)-1:] != '/'
            and request_path[len(request_path)-5:] == '.html'
        ):

            request_path = request_path

        print('DEBUG consructed path:' + request_path)

        assert request_path in self.source_files, (
            f"hyperlink [{str(data['request_path'])}] that was reconstructed to[{request_path}] "
            "does not exist. This link was found "
            f"within the following pages [{str(data['source_files'])}]"
        )


    def teardown_method(self):
        pass

    def teardown_class(self):
        del self.data

