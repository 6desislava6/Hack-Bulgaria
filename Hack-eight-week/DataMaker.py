import sqlite3


class DataMaker:

    def __init__(self):
        self.db = sqlite3.connect('mydb')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
            users(id INTEGER PRIMARY KEY, name TEXT,
                       github TEXT)''')
        self.__make_user_table()
        self.__make_courses_table()
        self.__make_relation_table()

    def __make_user_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
            users(id INTEGER PRIMARY KEY, name TEXT,
                       github TEXT)''')
        self.db.commit()

    def __make_courses_table(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS
             courses(id INTEGER PRIMARY KEY, name TEXT)''')
        self.db.commit()

    def __make_relation_table(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Students_To_Course(student_id INTEGER,
              course_id INTEGER,
              FOREIGN KEY(student_id) REFERENCES Students(id),
              FOREIGN KEY(course_id) REFERENCES Courses(id))''')
        self.db.commit()

    def add_user(self, user):
        name = user.name
        github = user.github
        courses = user.courses

        self.cursor.execute('''INSERT INTO users(name, github)
                  VALUES(?,?)''', (name, github))

        # adding to third table
        self.db.commit()
        student_id = self.cursor.lastrowid

        for course in courses:
            self.cursor.execute('''SELECT id FROM courses
                WHERE name = ?''', (course['name'], ))
            course_id = self.cursor.fetchone()

            self.cursor.execute('''INSERT INTO Students_To_Course(student_id, course_id)
                  VALUES(?,?)''', (student_id, course_id[0]))
        self.db.commit()

    def add_course(self, course_name):
        self.cursor.execute('''INSERT INTO courses(name)
            VALUES(?)''', (course_name, ))
        self.db.commit()

    def list_users(self):
        self.cursor.execute("SELECT id, name, github FROM users")
        return self.cursor.fetchall()

    def list_courses(self):
        self.cursor.execute("SELECT id, name FROM courses")
        return self.cursor.fetchall()

    def show_user(self, id_user):
        self.cursor.execute('''SELECT * FROM users
                WHERE id = ?''', (id_user, ))
        info = self.cursor.fetchone()
        name = info['name']
        github = info['github']
        self.cursor.execute('''SELECT * FROM Students_To_Course
            where student_id = ?''', (id_user, ))
        info = self.cursor.fetchall()
        courses = []
        courses_names = []

        for line in info:
            courses.append(line['course_id'])

        for id_course in courses:
            self.cursor.execute('''SELECT * FROM Courses
                where id = ?''', (id_course, ))
            info = self.cursor.fetchone()
            courses_names.append(info['name'])

        return [name, github, courses_names]

    def show_course_users(self, course_id):
        self.cursor.execute('''SELECT * from Students_To_Course JOIN users
         ON Students_To_Course.student_id = users.id
         WHERE course_id = ?''', (course_id, ))
        table_course = self.cursor.fetchall()
        names = []
        for line in table_course:
            names.append(line['name'])
        return names
