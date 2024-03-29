import unittest
from your_project.models import YourModel

class TestYourModelFindByName(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary resources before running the test case
        pass

    def tearDown(self):
        # Clean up any resources after running the test case
        pass

    def test_find_existing_item_by_name(self):
        # Create some sample data with specific names
        sample_data_1 = {'id': 1, 'name': 'Item 1', 'description': 'This is item 1.'}
        sample_data_2 = {'id': 2, 'name': 'Item 2', 'description': 'This is item 2.'}
        YourModel.create(**sample_data_1)
        YourModel.create(**sample_data_2)

        # Find items by name
        found_items = YourModel.find_by_name('Item 1')

        # Assert that the number of found items matches the expected number
        self.assertEqual(len(found_items), 1)

        # Assert that the found item's attributes match the sample data
        self.assertIn(sample_data_1, found_items)

    def test_find_non_existing_item_by_name(self):
        # Try to find items with a name that doesn't exist in the database
        found_items = YourModel.find_by_name('Non-existing Item')

        # Assert that no items were found
        self.assertEqual(len(found_items), 0)

if __name__ == '__main__':
    unittest.main()
