import unittest
from your_project import app

class TestDeleteRoute(unittest.TestCase):
    def setUp(self):
        # Initialize the Flask test client
        self.app = app.test_client()

    def tearDown(self):
        # Clean up any resources after running the test case
        pass

    def test_delete_route(self):
        # Make a DELETE request to the delete route
        response = self.app.delete('/items/1')

        # Check if the status code is 200 (OK) or 204 (No Content) based on your implementation
        self.assertIn(response.status_code, [200, 204])

        # Optionally, make a GET request to retrieve the item and assert its absence

if __name__ == '__main__':
    unittest.main()
