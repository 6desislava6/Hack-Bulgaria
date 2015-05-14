import sqlite3
from Client import Client
import re
import hashlib
import datetime
import os


class sql_manager:
    MIN_LENGTH = 8
    BANNED_MINUTES = 1

    @staticmethod
    def create_from_db_and_sql(db_name, create_sql, drop_sql, create_if_exists=False):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        # If it doesn't exist, make it
        if not os.path.exists(db_name) or create_if_exists:

            with open(drop_sql, 'r') as f:
                cursor.executescript(f.read())
                conn.commit()

        with open(create_sql, 'r') as g:
            cursor.executescript(g.read())
            conn.commit()
        return sql_manager(conn)

    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()
        self.create_clients_table()
        self.create_banned_table()
        self.create_tan_table()

    @classmethod
    def validate_password(cls, password):
        enough_symbols = len(password) >= cls.MIN_LENGTH
        are_there_symbols = re.search('[\-\/\@\?\!\,\.\#\&\*]+', password)
        are_there_numbers = re.search('\d+', password)
        are_there_capitals = re.search('[A-Z]+', password)
        if are_there_capitals and are_there_numbers and are_there_symbols and enough_symbols:
            return True
        return False

    @staticmethod
    def hash_password(password):
        hash_object = hashlib.sha1(password.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig

    def create_clients_table(self):
        create_query = '''create table if not exists
            clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT,
                    balance REAL DEFAULT 0,
                    message TEXT,
                    email TEXT)'''

        self.cursor.execute(create_query)

    def change_message(self, new_message, logged_user):
        update_sql = "UPDATE clients SET message = ? WHERE id = ?"
        self.cursor.execute(update_sql, (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)

    def change_pass(self, new_pass, logged_user):
        update_sql = "UPDATE clients SET password = ? WHERE id = ?"
        self.cursor.execute(update_sql, (sql_manager.hash_password(new_pass), logged_user.get_id()))
        self.conn.commit()

    def register(self, username, password):
        if self.validate_password(password):
            hashed_password = self.hash_password(password)
            insert_sql = """insert into clients
            (username, password) values (?, ?)"""
            self.cursor.execute(insert_sql, (username, hashed_password))
            self.conn.commit()
            return True
        else:
            return False

    def login(self, username, password):
        select_query = """SELECT id, username, balance, message, email
        FROM clients WHERE username = ?
        AND password = ? LIMIT 1"""

        hashed_password = self.hash_password(password)
        self.cursor.execute(select_query, (username, hashed_password))
        user = self.cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3], user[4])
        else:
            return False

    def create_banned_table(self):
        create_query = '''create table if not exists
            banned(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    date_banned DATE,
                    FOREIGN KEY (user_id) REFERENCES clients(user_id))'''

        self.cursor.execute(create_query)
        self.conn.commit()

    def add_banned(self, username):
        self.create_banned_table()
        self.cursor.execute("""SELECT id FROM clients
        WHERE username = ?""", (username, ))
        user_id = self.cursor.fetchone()[0]
        date_banned = datetime.datetime.now()

        insert_sql = "insert into banned (user_id, date_banned) values (?, ?)"
        self.cursor.execute(insert_sql, (user_id, date_banned))
        self.conn.commit()

    def show_banned(self):
        return self.cursor.execute("""SELECT username
            FROM clients JOIN banned
            ON clients.id = banned.user_id""")

    def update_banned(self):
        time = datetime.datetime.now() - datetime.timedelta(minutes=sql_manager.BANNED_MINUTES)
        self.cursor.execute("""DELETE FROM banned
            WHERE date_banned <= ? """, (time, ))
        self.conn.commit()

    def change_email(self, new_email, logged_user):
        update_sql = "UPDATE clients SET email = ? WHERE id = ?"
        self.cursor.execute(update_sql, (new_email, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_email(new_email)

    def get_hashed_psd(self, username):
        select_query = """SELECT password
        FROM clients
        WHERE username = ?"""
        self.cursor.execute(select_query, (username, ))
        return self.cursor.fetchone()[0]

    def reset_password(self, username, new_pass):
        update_sql = "UPDATE clients SET password = ? WHERE username = ?"
        self.cursor.execute(update_sql, (sql_manager.hash_password(new_pass), username))
        self.conn.commit()

    def get_email(self, username):
        select_query = """SELECT email
        FROM clients WHERE username = ?"""
        self.cursor.execute(select_query, (username, ))
        return self.cursor.fetchone()[0]

    def create_tan_table(self):
        create_query = '''create table if not exists
            tans(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    tan TEXT,
                    FOREIGN KEY (user_id) REFERENCES clients(user_id))'''

        self.cursor.execute(create_query)
        self.conn.commit()

    def add_tan(self, username, tan):
        select_query = """SELECT id
        FROM clients WHERE username = ? """
        self.cursor.execute(select_query, (username, ))
        user_id = self.cursor.fetchone()[0]
        insert_sql = """INSERT INTO tans (user_id, tan) values (?, ?)"""
        self.cursor.execute(insert_sql, (user_id, tan))
        self.conn.commit()

    def delete_tan(self, username, tan):
        select_query = """DELETE
        FROM tans WHERE tan = ? AND username = ?"""
        self.cursor.execute(select_query, (tan, username, ))
        self.conn.commit()

    def deposit(self, logged_user, money_amount):
        money = self.get_current_balance(logged_user) + money_amount
        update_sql = "UPDATE clients SET balance = ? WHERE username = ?"
        self.cursor.execute(update_sql, (money, logged_user.get_username()))
        self.conn.commit()

    def get_current_balance(self, logged_user):
        select_query = """SELECT balance
        FROM clients
        WHERE username = ?"""
        self.cursor.execute(select_query, (logged_user.get_username(), ))
        return float(self.cursor.fetchone()[0])

    def withdraw(self, logged_user, money_amount):
        money = self.get_current_balance(logged_user) - money_amount
        if money < 0:
            return False
        update_sql = "UPDATE clients SET balance = ? WHERE username = ?"
        self.cursor.execute(update_sql, (money, logged_user.get_username()))
        self.conn.commit()
        return True

    def check_TAN_code(self, logged_user, TAN_code):
        select_query = """SELECT Count(id)
        FROM tans
        WHERE user_id = ? AND tan = ?"""
        self.cursor.execute(select_query, (self.get_user_id(logged_user), TAN_code ))
        return self.cursor.fetchone()[0]

    def delete_TAN_code(self, logged_user, TAN_code):
        delete_query = """DELETE FROM tans
        WHERE tan = ? AND user_id = ?"""
        self.cursor.execute(delete_query, (TAN_code, self.get_user_id(logged_user)))
        self.conn.commit()

    def get_user_id(self, logged_user):
        select_query = """SELECT id FROM clients
        WHERE username = ?"""
        self.cursor.execute(select_query, (logged_user.get_username(), ))
        return self.cursor.fetchone()[0]
