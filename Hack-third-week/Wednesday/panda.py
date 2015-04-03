import re


class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.gender = gender
        is_valid = is_valid_email(email)
        if is_valid:
            self.email = email
        else:
            raise ValueError

    def __str__(self):
        return self.name

    def __eq__(self, another):
        equal_names = (self.get_name() == another.get_name())
        equal_emails = (self.get_email() == another.get_email())
        equal_genders = (self.get_gender() == another.get_gender())
        return equal_names and equal_emails and equal_genders

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return 'Panda({}, {}, {})'.format(self.name, self.email, self.gender)

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def check_isMale(self):
        return self.gender == 'male'

    def check_isFemale(self):
        return self.gender == 'female'


def is_valid_email(email):
    if re.search('([^@|\s]+@[^@]+\.[^@|\s]+)', email) == None:
        return False
    else:
        return re.search('([^@|\s]+@[^@]+\.[^@|\s]+)', email).group() == email
