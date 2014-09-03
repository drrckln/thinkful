import random
import unittest

class ItemCostTest(unittest.TestCase):
    def test1(self):
        cost = 100
        discount = 10
        amount = 30
        price = int((cost * (1 - (discount / 100)))) - amount
        self.assertEqual(price, 6)

if __name__ == '__main__':
    unittest.main()
