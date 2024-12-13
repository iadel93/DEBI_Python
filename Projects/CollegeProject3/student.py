from base_classes import Person

class Student(Person):
    def __init__(self, name, id:str, age, gender):
        super().__init__(name, id, age, gender)
        self.courses = []
        self.lectures = []
        self.labs = []
        self.GPA = None

    def Register(self, course):
        course.AddStudent(self)
        self.courses.append(course)

    def Drop(self, course):
        course.RemoveStudent(self)
        for i in range(len(self.courses)):
            if self.courses[i].id == course.id:
                self.courses.pop(i)
                break


    def Attend(self, course, date):
        session = course.AttendStudent(self, date)
        if session != None:
            if session.type == "Lecture":
                self.lectures.append(session)
            else:
                self.labs.append(session)


    def ListLectures(self):
        for lecture in self.lectures:
            print(lecture)

    def ListLabs(self):
        for lab in self.labs:
            print(lab)

    def ListCourses(self):
        for course in self.courses:
            print(course)


