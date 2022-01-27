import pytest

from conftest import Data

class Test:

    data = Data()

    def setup_method(self):

        self.approved_external_requests = {
            'gitlab.com': [
                'api/v4/projects/nofusscomputing%2Finfrastructure%2Fwebsite',
                'uploads/-/system/user/avatar/4125177/avatar.png'
            ]
        }


    @pytest.mark.parametrize(
        argnames='data', 
        argvalues=[link for url_id, link in data.test_data['page_load_resource_links'].items() if link['request_protocol'][0:4] =='http'], 
        ids=[url_id for url_id, link in data.test_data['page_load_resource_links'].items() if link['request_protocol'][0:4] =='http']
    )
    def test_page_external_requests(self, data):

            check_url = data['url']

            assert data['request_protocol'] == 'https', f"Insecure Request to domain [{data['request_path']}] in source files [{data['source_files']}]"

            assert data['domain'] in self.approved_external_requests, f"A request is being made to a non-approved domain [{data['domain']}] path [{data['request_path']}] in source files [{data['source_files']}]"

            assert data['request_path'] in self.approved_external_requests[data['domain']], f"A request is being made to a non-approved path [{data['request_path']}] on domain [{data['domain']}] in source files [{data['source_files']}]"



    def teardown_method(self):
        pass

