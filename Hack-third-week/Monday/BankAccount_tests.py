import unittest
from BankAccount import BankAccount


class TestBankAccout(unittest.TestCase):

    def setUp(self):
        self.name = "Rado"
        self.amount = 0
        self.currency = '$'
        self.my_account = BankAccount(self.name, self.amount, self.currency)
        self.deposited_money = 1000
        self.deposited_money_negative = -1000
        self.withdrawed_money_true = 500
        self.withdrawed_money_false = 1000
        self.transfered_money_true = 500
        self.transfered_money_false = 2000

    def test_init(self):
        self.assertTrue(isinstance(self.my_account, BankAccount))
        self.assertEqual(self.my_account.name, self.name)
        self.assertEqual(self.my_account.amount, self.amount)
        self.assertEqual(self.my_account.currency, self.currency)

    def test_deposit(self):
        current_balance = self.my_account.balance()
        self.my_account.deposit(self.deposited_money)
        self.assertEqual(
            self.my_account.amount, current_balance + self.deposited_money)
        with self.assertRaises(ValueError):
            self.my_account.deposit(self.deposited_money_negative)

    def test_balance(self):
        self.assertEqual(self.my_account.balance(), self.my_account.amount)

    def test_withdraw(self):
        self.my_account.amount = 1000
        self.assertTrue(self.my_account.withdraw(self.withdrawed_money_true))
        self.assertFalse(self.my_account.withdraw(self.withdrawed_money_false))
        self.my_account.withdraw(self.withdrawed_money_false)
        self.my_account.amount = 1000
        current_balance = self.my_account.balance()
        self.assertEqual(
            self.my_account.balance(), current_balance)
        current_balance = self.my_account.balance()
        self.my_account.withdraw(self.withdrawed_money_true)
        self.assertEqual(
            self.my_account.balance(), current_balance - self.withdrawed_money_true)

    def test_str(self):
        wanted_result = "Bank account for {} with balance of {}{}".format(
            self.my_account.name, self.my_account.amount, self.my_account.currency)
        self.assertEqual(str(self.my_account), wanted_result)

    def test_int(self):
        self.assertEqual(int(self.my_account), self.my_account.balance())

    def test_transfer_to(self):
        self.my_account.amount = 1000
        # CHECK CURRENCY
        ivo = BankAccount("Ivo", 0, "BGN")
        self.assertFalse(self.my_account.transfer_to(ivo, 600))
        ivo.currency = '$'
        # CHECK IF MONEY IS ENOUGH
        self.assertFalse(
            self.my_account.transfer_to(ivo, self.transfered_money_false))
        self.assertTrue(
            self.my_account.transfer_to(ivo, self.transfered_money_true))
        # CHECK IF MONEY HAS CHANGED, TRANSFERED
        ivo.amount = 0
        self.my_account.amount = 1000
        self.my_account.transfer_to(ivo, 200)
        self.assertEqual(
            self.my_account.balance(), 800)
        self.assertEqual(
            ivo.balance(), 200)

    def test_history(self):
        # Account Creation
        self.assertEqual(self.my_account.history()[0], 'Account was created')
        # Deposit
        self.my_account.deposit(1000)
        trueString = 'Deposited 1000' + self.my_account.currency
        self.assertEqual(self.my_account.history()[-1], trueString)
        # Balance
        self.my_account.balance()
        trueString = 'Balance check -> ' + \
            str(self.my_account.balance()) + self.my_account.currency
        self.assertEqual(self.my_account.history()[-1], trueString)
        # Int transformation
        trueString = '__int__ check -> ' + \
            str(self.my_account.balance()) + self.my_account.currency
        int(self.my_account)
        self.assertEqual(self.my_account.history()[-1], trueString)
        # Successfull withdraw
        self.my_account.withdraw(500)
        trueString = '500' + self.my_account.currency + \
            ' was withdrawed'
        self.assertEqual(self.my_account.history()[-1], trueString)
        # Failed withdraw
        self.my_account.withdraw(1000)
        trueString = 'Withdraw for {}{} failed.'.format(
            1000, self.my_account.currency)
        self.assertEqual(self.my_account.history()[-1], trueString)
        # Transfer
        ivo = BankAccount("Ivo", 0, "$")
        self.my_account = BankAccount("Rado", 1000, "$")
        self.my_account.transfer_to(ivo, 500)
        trueString_Rado = 'Transfer to {} for {}{}'.format(
            ivo.name, 500, self.my_account.currency)
        trueString_Ivo = 'Transer from {} for {}{}'.format(
            self.my_account.name, 500, ivo.currency)
        self.assertEqual(self.my_account.history()[-1], trueString_Rado)
        self.assertEqual(ivo.history()[-1], trueString_Ivo)
if __name__ == '__main__':
    unittest.main()
