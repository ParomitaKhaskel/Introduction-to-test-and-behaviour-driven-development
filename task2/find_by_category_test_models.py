import unittest
from your_project.models import YourModel

class TestYourModelFindByCategory(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary resources before running the test case
        pass

    def tearDown(self):
        # Clean up any resources after running the test case
        pass

    def test_find_existing_items_by_category(self):
        # Create some sample data with specific categories
        sample_data_1 = {'id': 1, 'name': 'Item 1', 'category': 'Category A', 'description': 'This is item 1 in Category A.'}
        sample_data_2 = {'id': 2, 'name': 'Item 2', 'category': 'Category B', 'description': 'This is item 2 in Category B.'}
        sample_data_3 = {'id': 3, 'name': 'Item 3', 'category': 'Category A', 'description': 'This is item 3 in Category A.'}
        YourModel.create(**sample_data_1)
        YourModel.create(**sample_data_2)
        YourModel.create(**sample_data_3)

        # Find items by category
        found_items = YourModel.find_by_category('Category A')

        # Assert that the number of found items matches the expected number
        self.assertEqual(len(found_items), 2)

        # Assert that the found items' attributes match the sample data
        self.assertIn(sample_data_1, found_items)
        self.assertIn(sample_data_3, found_items)

    def test_find_non_existing_items_by_category(self):
        # Try to find items with a category that doesn't exist in the database
        found_items = YourModel.find_by_category('Non-existing Category')

        # Assert that no items were found
        self.assertEqual(len(found_items), 0)

if __name__ == '__main__':
    unittest.main()
