import pytest

from conftest import Data

class Test:

    data = Data()

    def setup_method(self):
        pass


    @pytest.mark.parametrize(
        argnames='data', 
        argvalues=[link for url_id, link in data.test_data['hyperlinks'].items() if link['request_protocol'][0:4] =='http'], 
        ids=[url_id for url_id, link in data.test_data['hyperlinks'].items() if link['request_protocol'][0:4] =='http']
    )
    def test_hyperlink_alive_check(self, data):
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

        
    def teardown_method(self):
        pass

    def teardown_class(self):
        del self.data

