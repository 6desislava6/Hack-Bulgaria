import getpass


class IO:

    def __init__(self, controller):
        self.controller = controller

    def main_menu(self):
        print(self.controller.WELCOME_MESSAGE)
        command = input("$$$>")
        while command != 'exit':
            if command == 'register':
                self.register()

            elif command == 'login':
                self.login()

            elif command == 'help':
                self.help()

            elif command == 'reset-password':
                self.reset_password()

            else:
                print("Not a valid command")
            command = input("$$$>")

    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        command = input("Logged>>")
        while command != 'exit':

            if command == 'info':
                self.show_info(logged_user)

            elif command == 'changepass':
                self.change_pass(logged_user)

            elif command == 'change-message':
                self.change_messagel(logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'change-email':
                self.change_email(logged_user)

            elif command == 'show-email':
                self.show_email(logged_user)

            elif command == 'get-tan':
                self.make_tans(logged_user)

            elif command == 'withdraw':
                self.withdraw(logged_user)

            elif command == 'deposit':
                self.deposit(logged_user)

            elif command == 'help':
                self.help_user()

            command = input("Logged>>")

    def register(self):
        username = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        reg_status = self.controller.register(username, password)
        while not reg_status[0]:
            print(reg_status[1])
            password = getpass.getpass(prompt="Enter your password: ")
            reg_status = self.controller.register(username, password)
        print(reg_status[1])

    def login(self):
        username = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        login_status = self.controller.login(username, password)
        if login_status[0]:
            self.logged_menu(login_status[0])
        print(login_status[1])

    def help(self):
        for line in self.controller.help():
            print(line)

    def ban_user(self, username):
        print(self.controller.ban_user(username))

    def show_info(self, logged_user):
        for line in self.controller.show_info(logged_user):
            print(line)

    def change_pass(self, logged_user):
        new_pass = getpass.getpass(prompt="Enter your new password: ")
        self.controller.change_pass(new_pass, logged_user)

    def change_message(self, logged_user):
        new_message = input("Enter your new message: ")
        self.controller.change_message(new_message, logged_user)

    def help_user(self):
        for line in self.controller.help_user():
            print(line)

    def change_email(self, logged_user):
        new_email = input('Type new email: ')
        self.controller.change_email(new_email, logged_user)
        print('Changed email!')

    def show_email(self, logged_user):
        print('Your email is:')
        print(self.controller.show_email(logged_user))

    def reset_password(self):
        username = input('Your username> ')
        user_email = input('Your email> ')
        valid_email = self.controller.validate_email(username, user_email)
        if valid_email:
            self.controller.send_email(username, user_email)
            response = input('Enter code from email> ')
            validated = self.controller.check_user_response(username, response)
            if validated:
                new_pass = getpass.getpass(prompt="Enter your new password: ")
                print(self.controller.reset_password(username, new_pass))
            else:
                print('Wrong code!')
        else:
            print('Invalid email!')

    def make_tans(self, logged_user):
        print(self.controller.make_tans(logged_user))

    def deposit(self, logged_user):
        money = float(input('Enter amount: '))
        TAN_code = input('Enter TAN: ')
        print(self.controller.deposit(logged_user, money, TAN_code))

    def withdraw(self, logged_user):
        money = float(input('Enter amount: '))
        TAN_code = input('Enter TAN: ')
        print(self.controller.withdraw(logged_user, money, TAN_code))

