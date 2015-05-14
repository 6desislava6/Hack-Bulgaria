import sys
import unittest
import os

sys.path.append("..")

from Controller import Controller
from sql_manager import sql_manager
from settings_tests import db_name, create_sql, drop_sql


class ControllerTest(unittest.TestCase):

    def setUp(self):
        self.manager = sql_manager.create_from_db_and_sql(db_name, create_sql, drop_sql, create_if_exists=True)
        self.controller = Controller(self.manager)
        self.controller.register('a', '123456A#')

    def tearDown(self):
        self.manager.cursor.execute('DROP TABLE clients')
        self.manager.cursor.execute('DROP TABLE banned')

    @classmethod
    def tearDownClass(cls):
        os.remove(db_name)

    def test_register(self):
        result = self.controller.register('b', '123456A#')
        self.assertTrue(result[0])
        self.assertTrue(result[1] == 'Registration Successfull')
        result = self.controller.register('c', '111')
        self.assertFalse(result[0])

    def test_login(self):
        result = self.controller.login('a', '123456A#')
        self.assertEqual(result[1], 'Login successfull!')
        result = self.controller.login('a', '12asdafd3456A#')
        self.assertEqual(result[1], 'Login failed!')
        self.assertFalse(result[0])

    def test_add_to_current_users_or_ban(self):
        self.controller.login('a', '1123456A#')
        self.assertEqual(self.controller.current_users['a'], 1)
        self.controller.login('a', '1123456A#')
        self.assertEqual(self.controller.current_users['a'], 2)
        self.controller.login('a', '1123456A#')
        self.controller.login('a', '1123456A#')
        self.controller.login('a', '1123456A#')
        self.controller.login('a', '1123456A#')
        banned = self.controller.manager.show_banned()
        for line in banned:
            self.assertEqual('a', line[0])
        self.assertTrue(self.controller.is_in_banned('a'))

    def test_deposit(self):
        logged_user = self.controller.manager.login('a', '123456A#')
        self.assertEqual(self.controller.deposit(logged_user, 20, 12), 'Transaction not successful - TAN is wrong... :(')

    def test_withdraw(self):
        logged_user = self.controller.manager.login('a', '123456A#')
        self.assertEqual(self.controller.withdraw(logged_user, 20, 12), 'Withdrawal not successful - TAN is wrong... :(')

if __name__ == '__main__':
    unittest.main()


