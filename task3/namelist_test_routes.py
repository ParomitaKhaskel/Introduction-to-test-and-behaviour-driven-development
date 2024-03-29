import unittest
from your_project import app
import json

class TestListByNameRoute(unittest.TestCase):
    def setUp(self):
        # Initialize the Flask test client
        self.app = app.test_client()

    def tearDown(self):
        # Clean up any resources after running the test case
        pass

    def test_list_by_name_route(self):
        # Make a GET request to the list by name route with a specific name
        response = self.app.get('/items?name=Sample')

        # Decode the response data from JSON
        data = json.loads(response.data.decode('utf-8'))

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Optionally, assert the content of the response data
        
        # For example, if the response data is expected to be a list of items:
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
