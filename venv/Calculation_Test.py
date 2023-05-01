import unittest


class TestCalculateTotal(unittest.TestCase):
    def test_no_items(self):
        self.assertEqual(calculate_total('NJ', []), 0)

    def test_wic_eligible_food(self):
        items = [
            {'name': 'Bread', 'price': 1.99, 'type': 'Wic Eligible food'},
            {'name': 'Milk', 'price': 3.99, 'type': 'Wic Eligible food'}
        ]
        self.assertEqual(calculate_total('PA', items), 5.98)

    def test_clothing_no_tax(self):
        items = [
            {'name': 'T-shirt', 'price': 19.99, 'type': 'Clothing'},
            {'name': 'Jeans', 'price': 39.99, 'type': 'Clothing'}
        ]
        self.assertEqual(calculate_total('NJ', items), 59.98)

    def test_clothing_fur_tax(self):
        items = [
            {'name': 'Fur coat', 'price': 399.99, 'type': 'Clothing'},
            {'name': 'Sweater', 'price': 59.99, 'type': 'Clothing'}
        ]
        self.assertEqual(calculate_total('NJ', items), 478.99)

    def test_default_tax(self):
        items = [
            {'name': 'TV', 'price': 399.99, 'type': 'everything else'},
            {'name': 'Laptop', 'price': 999.99, 'type': 'everything else'}
        ]
        self.assertEqual(calculate_total('DE', items), 1459.96)
