from IO import IO
from Controller import Controller
from settings import db_name, create_sql, drop_sql
from sql_manager import sql_manager


def main():
    manager = sql_manager.create_from_db_and_sql(db_name, create_sql, drop_sql, create_if_exists=False)
    manager.create_clients_table()
    controller = Controller(manager)
    io = IO(controller)
    io.main_menu()

if __name__ == '__main__':
    main()
