import unittest
from your_project import app
import json

class TestReadRoute(unittest.TestCase):
    def setUp(self):
        # Initialize the Flask test client
        self.app = app.test_client()

    def tearDown(self):
        # Clean up any resources after running the test case
        pass

    def test_read_route(self):
        # Make a GET request to the read route
        response = self.app.get('/items/1')

        # Decode the response data from JSON
        data = json.loads(response.data.decode('utf-8'))

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the expected data
        self.assertIn('id', data)
        self.assertIn('name', data)
        self.assertIn('description', data)
        # Add more assertions as needed based on your response data structure

if __name__ == '__main__':
    unittest.main()
