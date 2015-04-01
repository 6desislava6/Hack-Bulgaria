import unittest
from cashdesk import Bill


class BillTest(unittest.TestCase):
    def setUp(self):
        self.my_bill = Bill(5)

    def test_create_new_bill_instance(self):
        self.assertTrue(isinstance(self.my_bill, Bill))

    def test_valid_amount(self):
        self.assertEqual(self.my_bill.amount, 5)

    def test_valid_str(self):
        self.assertEqual(str(self.my_bill), 'A {}$ bill' .format(my_bill.amount))

if __name__ == '__main__':
    unittest.main()
