from email_sender import Email_Sender
from GenerateTans import GenerateTans


class Controller:
    MESSAGE_NOT_REGISTERED= """Your password is not strong enough!
It should be more than 8 symbols,containing capital letters, numbers
and at least one special symbol (-/@?!,.#&*)
and it must not be the same as your username!"""
    current_users = {}
    MAX_ATTEMPTS = 5
    WELCOME_MESSAGE = """Welcome to our bank service. You are not logged in.
Please register or login"""
    TANS_COUNT = 10

    def __init__(self, manager):
        self.manager = manager

    def register(self, username, password):
        if self.manager.register(username, password):
            return [True, 'Registration Successfull']
        return [False, Controller.MESSAGE_NOT_REGISTERED]

    def login(self, username, password):
        self.update_banned()
        logged_user = self.manager.login(username, password)

        if logged_user and not self.is_in_banned(logged_user.get_username()):
            return [logged_user, 'Login successfull!']
        else:
            self.add_to_current_users_or_ban(username)
            return [False, 'Login failed!']

    @staticmethod
    def help():
        return ["login - for logging in!", "register - for creating new account!", "exit - for closing program!"]

    def add_to_current_users_or_ban(self, username):
        if username in Controller.current_users:
            Controller.current_users[username] += 1
            if Controller.current_users[username] > Controller.MAX_ATTEMPTS:
                self.ban_user(username)
        else:
            Controller.current_users.update({username: 1})

    @staticmethod
    def show_info(logged_user):
        result = ["You are: " + logged_user.get_username()]
        result.append("Your id is: " + str(logged_user.get_id()))
        result.append(
            "Your balance is:" + str(logged_user.get_balance()) + '$')
        return result

    def ban_user(self, username):
        self.manager.add_banned(username)
        return "{} is banned!".format(username)

    def change_pass(self, new_pass, logged_user):
        self.manager.change_pass(new_pass, logged_user)

    def change_message(self, new_message, logged_user):
        self.manager.change_message(new_message, logged_user)

    @staticmethod
    def help_user():
        result = ["info - for showing account info"]
        result.append("changepass - for changing passowrd")
        result.append("change-message - for changing users message")
        result.append("show-message - for showing users message")
        return result

    def is_in_banned(self, username):
        all_banned_raw = self.manager.show_banned()
        all_banned = []
        for line in all_banned_raw:
            all_banned.append(line[0])
        return username in all_banned

    def update_banned(self):
        self.manager.update_banned()

    def change_email(self, new_email, logged_user):
        self.manager.change_email(new_email, logged_user)

    def show_email(self, logged_user):
        return logged_user.get_email()

    def send_email(self, username, user_email):
        hashed = self.manager.get_hashed_psd(username)
        Email_Sender.send_email(user_email, hashed)

    def check_user_response(self, username, user_response):
        return user_response == self.manager.get_hashed_psd(username)

    def reset_password(self, username, new_pass):
        self.manager.reset_password(username, new_pass)
        return 'Successfully reset password!'

    def validate_email(self, username, email):
        return email == self.manager.get_email(username)

    def make_tans(self, logged_user):
        tans = GenerateTans.generate_tans(Controller.TANS_COUNT)
        email_text = ''
        for tan in tans:
            self.manager.add_tan(logged_user.get_username(), tan)
            email_text += str(tan) + '\n'
        if logged_user.get_email() is None:
            return 'Invalid email!'
        Email_Sender.send_email(logged_user.get_email(), email_text)
        return 'TANs sent to email'

    def deposit(self, logged_user, money, TAN_code):
        if self.manager.check_TAN_code(logged_user, TAN_code):
            self.manager.delete_TAN_code(logged_user, TAN_code)
            self.manager.deposit(logged_user, money)
            return 'Transaction successful!'
        return 'Transaction not successful - TAN is wrong... :('

    def withdraw(self, logged_user, money, TAN_code):
        if self.manager.check_TAN_code(logged_user, TAN_code):
            self.manager.delete_TAN_code(logged_user, TAN_code)
            is_successful = self.manager.withdraw(logged_user, money)
            if not is_successful:
                return 'Withdrawal cannot be completed! Not enough money!'
            return 'Withdrawal successful!'
        return 'Withdrawal not successful - TAN is wrong... :('
