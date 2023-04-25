class School():
    def __init__(self, school):
        self.school = school
class Department(School):
    def __init__(self, school, department):
        School.__init__(self, school)
        self.department = department
class Courses(Department):
    def __init__(self, school, department, courses):
        Department.__init__(self, school, department)
        self.courses = courses

    def print(self):
        print("This is ", self.school, self.department, self.courses)

cs1302 = Courses('Georgia State University', 'Computer Science Department', 'course 1302')
cs1302.print()
