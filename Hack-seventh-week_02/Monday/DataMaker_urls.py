import sqlite3


class DataMaker:

    def __init__(self, filename):
        self.db = sqlite3.connect(filename)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS urls(id INTEGER PRIMARY KEY, url TEXT, server TEXT)''')

    def add_server(self, url, server):
        self.cursor.execute('''INSERT INTO urls(url, server) VALUES(?, ?)''', (url, server))
        self.db.commit()

    def list_urls_servers(self):
        return self.cursor.execute("SELECT id, url, server FROM urls;")
