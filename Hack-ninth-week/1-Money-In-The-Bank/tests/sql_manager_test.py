import sys
import unittest
import os
import datetime
import time
from settings_tests import db_name, create_sql, drop_sql

sys.path.append("..")

from sql_manager import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        self.manager = sql_manager.create_from_db_and_sql(db_name, create_sql, drop_sql, True)
        self.manager.create_clients_table()
        self.manager.register('Dinko', 'desiSLAVa81#?!-214')

    def tearDown(self):
        self.manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove(db_name)

    def test_register(self):
        self.manager.cursor.execute("""SELECT Count(*)
        FROM clients WHERE username = (?)
        AND password = (?)
        """, ('Dinko', self.manager.hash_password('desiSLAVa81#?!-214')))
        users_count = self.manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = self.manager.login('Dinko', 'desiSLAVa81#?!-214')
        self.assertEqual(logged_user.get_username(), 'Dinko')

    def test_login_wrong_password(self):
        logged_user = self.manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = self.manager.login('Dinko', 'desiSLAVa81#?!-214')
        new_message = "podaivinototam"
        self.manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = self.manager.login('Dinko', 'desiSLAVa81#?!-214')
        new_password = 'desiSLAVa81#?!-21466'
        self.manager.change_pass(new_password, logged_user)

        logged_user_new_password = self.manager.login('Dinko', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Dinko')

    def test_add_banned(self):
        self.manager.add_banned('Dinko')
        self.manager.cursor.execute("""SELECT username, date_banned FROM
        banned JOIN clients
        ON clients.id = banned.user_id
        WHERE username = ?""", ('Dinko', ))
        data = self.manager.cursor.fetchone()
        name = data[0]
        date = data[1]
        self.assertEqual('Dinko', name)
        self.assertTrue(date <= str(datetime.datetime.now()))

    def test_update_banned(self):
        self.manager.add_banned('Dinko')
        time.sleep(60)
        self.manager.update_banned()
        self.manager.cursor.execute("""SELECT count(id) FROM banned""")
        count = self.manager.cursor.fetchone()[0]
        self.assertEqual(0, count)

    def test_email(self):
        logged_user = self.manager.login('Dinko', 'desiSLAVa81#?!-214')
        self.manager.change_email('aaa', logged_user)
        self.assertEqual('aaa', logged_user.get_email())

if __name__ == '__main__':
    unittest.main()
