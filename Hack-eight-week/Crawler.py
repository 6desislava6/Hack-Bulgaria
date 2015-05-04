import requests
from User_and_Course_class import User
# import json

class Crawler:

    def __init__(self, url):
        site_response = requests.get(url)
        self.information = site_response.json()
        self.users = self.__set_users()
        self.courses = self.__set_courses()

    def __set_users(self):
        users = []
        for item in self.information:
            name = item["name"]
            github = item["github"]
            courses = item["courses"]
            users.append(User(name, github, courses))
        return users

    def get_users(self):
        return self.users

    def __set_courses(self):
        courses = set()
        for item in self.information:
            courses_of_user = item["courses"]
            for course in courses_of_user:
                courses.add(course["name"])
        return courses

    def get_courses(self):
        return self.courses
