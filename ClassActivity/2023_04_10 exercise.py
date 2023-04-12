class Student:
    def __init__(self, name, major, course):
        self.name = name
        self.major = major
        self.course = course
    def print(self):
        print('Your name is ', self.name)
        print('Your major is ', self.major)
        print('Your course is ', self.course)

Emma = Student('Emma', 'English', 'ENGL1102')
Emma.print