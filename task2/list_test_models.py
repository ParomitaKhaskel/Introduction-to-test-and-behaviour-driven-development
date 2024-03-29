import unittest
from your_project.models import YourModel

class TestYourModelListAll(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary resources before running the test case
        pass

    def tearDown(self):
        # Clean up any resources after running the test case
        pass

    def test_list_all_items(self):
        # Create some sample data to be listed
        sample_data_1 = {'id': 1, 'name': 'Item 1', 'description': 'This is item 1.'}
        sample_data_2 = {'id': 2, 'name': 'Item 2', 'description': 'This is item 2.'}
        YourModel.create(**sample_data_1)
        YourModel.create(**sample_data_2)

        # Retrieve all items from the database
        all_items = YourModel.list_all()

        # Assert that the number of retrieved items matches the expected number
        self.assertEqual(len(all_items), 2)

        # Assert that each item's attributes match the sample data
        self.assertIn(sample_data_1, all_items)
        self.assertIn(sample_data_2, all_items)

if __name__ == '__main__':
    unittest.main()
