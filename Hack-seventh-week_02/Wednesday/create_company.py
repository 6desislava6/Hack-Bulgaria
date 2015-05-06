from data_maker import DataMaker


class CommandIO:

    @staticmethod
    def make_initial_data_base(db):
        db.add_employee("Ivan Ivanov", 5000, 10000, "Software Developer")
        db.add_employee("Rado Rado", 500, 0, "Technical Support Intern")
        db.add_employee("Ivo Ivo", 10000, 100000, "CEO")
        db.add_employee("Petar Petrov", 3000, 1000, "Marketing Manager")
        db.add_employee("Maria Georgieva", 8000, 10000, "COO")

    @staticmethod
    def list_employees(db):
        empoyees = db.list_employees()
        for employee in empoyees:
            print('{} - {} - {}'.format(employee['id'], employee['name'], employee['position']))

    @staticmethod
    def add_employee(db):
        name = input('name>')
        monthly_salary = input('monthly_salary>')
        yearly_bonus = input('yearly_bonus>')
        position = input('position>')
        db.add_employee(name, monthly_salary, yearly_bonus, position)

    @staticmethod
    def monthly_spendings(db):
        print(db.monthly_spendings())

    @staticmethod
    def yearly_spendings(db):
        print(db.yearly_spendings())

    @staticmethod
    def delete_employee(db):
        id_employee = input('id>')
        db.delete_employee(id_employee)
        #print('Deleted ' + deleted)

    @staticmethod
    def update_employee(db):
        id_employee = input('id>')
        name = input('name>')
        monthly_salary = input('monthly_salary>')
        yearly_bonus = input('yearly_bonus>')
        position = input('position>')
        db.update_employee(id_employee, name, monthly_salary, yearly_bonus, position)

    @staticmethod
    def command(db, user_input):
        if user_input == 'list':
            CommandIO.list_employees(db)
        elif user_input == 'add':
            CommandIO.add_employee(db)
        elif user_input == 'monthly':
            CommandIO.monthly_spendings(db)
        elif user_input == 'yearly':
            CommandIO.yearly_spendings(db)
        elif user_input == 'delete':
            CommandIO.delete_employee(db)
        elif user_input == 'update':
            CommandIO.update_employee(db)
        else:
            print('Invalid command')

