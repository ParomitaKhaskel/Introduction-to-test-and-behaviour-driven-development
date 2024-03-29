import unittest
from your_project.models import YourModel

class TestYourModelFindByAvailability(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary resources before running the test case
        pass

    def tearDown(self):
        # Clean up any resources after running the test case
        pass

    def test_find_available_items(self):
        # Create some sample data with specific availability
        sample_data_1 = {'id': 1, 'name': 'Item 1', 'availability': True, 'description': 'This is item 1 and is available.'}
        sample_data_2 = {'id': 2, 'name': 'Item 2', 'availability': False, 'description': 'This is item 2 and is not available.'}
        sample_data_3 = {'id': 3, 'name': 'Item 3', 'availability': True, 'description': 'This is item 3 and is available.'}
        YourModel.create(**sample_data_1)
        YourModel.create(**sample_data_2)
        YourModel.create(**sample_data_3)

        # Find available items
        available_items = YourModel.find_by_availability(True)

        # Assert that the number of available items matches the expected number
        self.assertEqual(len(available_items), 2)

        # Assert that the available items' attributes match the sample data
        self.assertIn(sample_data_1, available_items)
        self.assertIn(sample_data_3, available_items)

    def test_find_unavailable_items(self):
        # Create some sample data with specific availability
        sample_data_1 = {'id': 1, 'name': 'Item 1', 'availability': True, 'description': 'This is item 1 and is available.'}
        sample_data_2 = {'id': 2, 'name': 'Item 2', 'availability': False, 'description': 'This is item 2 and is not available.'}
        sample_data_3 = {'id': 3, 'name': 'Item 3', 'availability': True, 'description': 'This is item 3 and is available.'}
        YourModel.create(**sample_data_1)
        YourModel.create(**sample_data_2)
        YourModel.create(**sample_data_3)

        # Find unavailable items
        unavailable_items = YourModel.find_by_availability(False)

        # Assert that the number of unavailable items matches the expected number
        self.assertEqual(len(unavailable_items), 1)

        # Assert that the unavailable item's attributes match the sample data
        self.assertIn(sample_data_2, unavailable_items)

if __name__ == '__main__':
    unittest.main()
