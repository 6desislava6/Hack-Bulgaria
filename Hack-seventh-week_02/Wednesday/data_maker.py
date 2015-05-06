
import sqlite3


class DataMaker:
    # ID_CELL = 'id'
    MONTHS = 12
    # NAME_CELL = 'name'
    # POSITION_CELL = 'position'

    def __init__(self):
        self.db = sqlite3.connect('mydb')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS company(id INTEGER PRIMARY KEY, name TEXT,
                       monthly_salary INTEGER, yearly_bonus yearly_bonus, position TEXT)''')

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
        self.db.commit()

    def list_employees(self):
        return self.cursor.execute("SELECT id, name, position FROM company;")

    def monthly_spendings(self):
        all_amount = 0
        spendings = self.cursor.execute("SELECT monthly_salary FROM company;")
        for money in spendings:
            all_amount += money[0]
        return all_amount

    def yearly_spendings(self):
        all_amount = 0
        bonuses = self.cursor.execute("SELECT yearly_bonus FROM company;")
        for money in bonuses:
            all_amount += money[0]
        all_amount += self.monthly_spendings() * DataMaker.MONTHS
        return all_amount

    def delete_employee(self, id_employee):
        empl = self.cursor.execute(
            '''SELECT name FROM company WHERE id = ? ''', (id_employee))
       # name = empl['name']
        self.cursor.execute(
            '''DELETE FROM company WHERE id = ? ''', (id_employee))
       # return name

    def update_employee(self, id_employee, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute('''UPDATE company SET name = ?,
                                    monthly_salary = ?,
                                     yearly_bonus= ?,
                                     position = ?
                        WHERE id = ? ''', (name, monthly_salary, yearly_bonus, position, id_employee))
