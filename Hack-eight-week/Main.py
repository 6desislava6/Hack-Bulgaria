from Crawler import Crawler
from DataMaker import DataMaker


def main():
    cr = Crawler('https://hackbulgaria.com/api/students/')
    db = DataMaker()
    users = cr.get_users()
    courses = cr.get_courses()

    # Making first table
    for course in courses:
        db.add_course(course)

    # Making second and third table
    for user in users:
        db.add_user(user)

if __name__ == '__main__':
    main()
