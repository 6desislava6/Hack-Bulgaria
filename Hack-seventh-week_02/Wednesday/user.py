from create_company import CommandIO
from data_maker import DataMaker


def main():
    db = DataMaker()
    user_input = input('command>')
    while user_input != 'exit':
        CommandIO.command(db, user_input)
        user_input = input('command>')

if __name__ == '__main__':
    main()
