class User:

    def __init__(self, name, github, courses):
        self.name = name
        self.github = github
        self.courses = courses

    def __repr__(self):
        return self.name
