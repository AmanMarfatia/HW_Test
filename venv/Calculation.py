import unittest
from production import calculate_total


class TestCalculateTotal(unittest.TestCase):

    def test_no_items(self):
        self.assertEqual(calculate_total('NJ', []), 0.0)

    def test_wic_food(self):
        records = [
            {'item_name': 'Orange', 'item_price': 2.0, 'item_type': 'Wic Eligible food'},
            {'item_name': 'Pizza', 'item_price': 10.0, 'item_type': 'Wic Eligible food'}

        ]
        self.assertEqual(calculate_total('PA', records), 0.0)

    def test_clothing_fur(self):
        records = [
            {'item_name': 'Canada Goose', 'item_price': 200.0, 'item_type': 'Clothing'}
        ]
        self.assertAlmostEqual(calculate_total('NJ', records), 212.0, places=2)

    def test_clothing_no_fur(self):
        records = [
            {'item_name': 'T-Shirt', 'item_price': 10.0, 'item_type': 'Clothing'}
        ]
        self.assertEqual(calculate_total('PA', records), 10.0)

    def test_default_tax_rate(self):
        records = [
            {'item_name': 'Phone', 'item_price': 500.0, 'item_type': 'Electronics'}
        ]
        self.assertAlmostEqual(calculate_total('DE', records), 500.0, places=2)

    def test_multiple_items(self):
        records = [
            {'item_name': 'Orange', 'item_price': 1.0, 'item_type': 'Wic Eligible food'},
            {'item_name': 'T-Shirt', 'item_price': 20.0, 'item_type': 'Clothing'},
            {'item_name': 'Phone', 'item_price': 500.0, 'item_type': 'Electronics'}
        ]
        self.assertAlmostEqual(calculate_total('NJ', records), 537.12, places=2)


if __name__ == '__main__':
    unittest.main()
