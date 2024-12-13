from base_classes import Person

class Student(Person):
    def __init__(self, name, id, age, level, major):
        super().__init__(name, id, age)
        self.level = level
        self.major = major
        self.courses = []


    def Register(self, course):
        self.courses.append(course)
        course.RegisterStudent(self)


    def Drop(self, course):
        course.DropStudent(self)
        for i in range(len(self.courses)):
            if self.courses[i].id == course.id:
                self.courses.pop(i)
                break

    def ListCourses(self):
        for course in self.courses:
            print(course)

    def CalculateGPA(self):
        pass

    def Attend(self, course, date):
        course.StudentAttendance(self, date)
        


    