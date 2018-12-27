import unittest
from bank_account import BankAccount, MinimumBalanceAccount

class AccountBalanceTestCase(unittest.TestCase):
    def setUp(self):
        self.account_silas = BankAccount()

    def test_balance(self):
        self.assertEqual(self.account_silas.balance, 3000, msg = "Account Balance invalid.")

    def test_deposit(self):
        self.account_silas.deposit(4000)
        self.assertEqual(self.account_silas.balance, 7000, msg = "Deposit method inaccurates")

    def test_withdraw(self):
        self.account_silas.withdraw(3000)
        self.assertEqual(self.account_silas.balance, 0, msg="withdraw method invalid.")

    def test_invalid_transaction(self):
        self.assertEqual(self.account_silas.withdraw(5000), 'invalid transaction', msg ='invalid transaction')

    def test_sub_class(self):
        self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg='Not True subclass')