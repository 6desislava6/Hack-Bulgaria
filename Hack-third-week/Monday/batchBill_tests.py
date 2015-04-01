import unittest
from cashdesk import Bill
from cashdesk import BillBatch


class TestBatchBill(unittest.TestCase):
    def setUp(self):
        values = [10, 20, 50, 100]
        self.bills = [Bill(value) for value in values]
        self.my_batch = BillBatch(self.bills)

    def test_init(self):
        self.assertTrue(isinstance(self.my_batch, BillBatch))
        self.assertEqual(self.my_batch.bills, self.bills)

    def test_iteration(self):
        self.assertEqual(self.my_batch[1], self.bills[1])

if __name__ == '__main__':
    unittest.main()
