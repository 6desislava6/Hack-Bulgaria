from Crawler import Crawler
from DataMaker import DataMaker


def make_database(db):
    cr = Crawler('https://hackbulgaria.com/api/students/')
    users = cr.get_users()
    courses = cr.get_courses()

    # Making first table
    for course in courses:
        db.add_course(course)

    # Making second and third table
    for user in users:
        db.add_user(user)


def print_instructions():
    print('Hello!')
    print('1. Make database')
    print('2. Show all users')
    print('3. Show all courses')
    print('4. Show specific user and the courses, which he/she goes to')
    print('5. Show all users going to specific course')
    print('exit by typing "exit"')
    print('Choose your command 1 - 5')


def main():
    db = DataMaker()
    print_instructions()
    # make_database(db)
    user_input = input('command>')
    while user_input != 'exit':
        if user_input == '1':
            print('Making database')
            make_database(db)

        elif user_input == '2':
            all_users = db.list_users()
            for user in all_users:
                name = user['name']
                id_user = user['id']
                github = user['github']
                print(("{}. {} -> {}").format(id_user, name, github))

        elif user_input == '3':
            all_courses = db.list_courses()
            for course in all_courses:
                id_course = course['id']
                name = course['name']
                print(("{}. {}").format(id_course, name))

        elif user_input == '4':
            print('Enter user id')
            id_user = input('user id>')
            info = db.show_user(int(id_user))
            print(("User's name is {}").format(info[0]))
            print(("User's github is {}").format(info[1]))
            print("User's courses:")
            for course in info[2]:
                print(course)
        elif user_input == '5':
            print('Enter course id')
            id_course = input('user id>')
            people_names = db.show_course_users(id_course)
            print(people_names)
        else:
            print('Invalid command!')
        user_input = input('command>')

if __name__ == '__main__':
    main()
