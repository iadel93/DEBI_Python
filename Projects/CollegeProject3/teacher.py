from base_classes import Person, Session

class Teacher(Person):
    def __init__(self, name, id, age, gender, salary):
        super().__init__(name, id, age, gender)
        self.courses = []
        self.lectures = []
        self.labs = []
        self.salary = salary

    def Teach(self, course):
        course.AddTeacher(self)
        self.courses.append(course)

    def Drop(self, course):
        course.RemoveTeacher()
        for i in range(len(self.courses)):
            if self.courses[i].id == course.id:
                self.courses.pop(i)
                break
        
    def ListCourses(self):
        for course in self.courses:
            print(course)

    def DeliverLecture(self,course,date):
        session = Session(
            date = date,
            type = "Lecture",
            course_name= course.name,
            teacher= self,
            building = "A1"
        )
        self.lectures.append(session)
        course.DeliverLecture(session)


    def DeliverLab(self, course, date):
        session = Session(
            date = date,
            type = "Lab",
            course_name= course.name,
            teacher= self,
            building = "A2"
        )
        self.labs.append(session)
        course.DeliverLab(session)