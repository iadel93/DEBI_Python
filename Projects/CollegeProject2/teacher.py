from base_classes import Person, Lecture


class Teacher(Person):
    def __init__(self, name, id, age, salary, department):
        super().__init__(name, id, age)
        self.salary = salary
        self.department = department
        self.courses = []
        self.total_credit_hours = 0
        self.lectures = {}



    def AddCourse(self, course):
        self.courses.append(course)
        self.total_credit_hours += course.credit_hours
        course.teacher = self


    def DropCourse(self, course):
        for i in range(len(self.courses)):
            if self.courses[i].id == course.id:
                self.courses.pop(i)
                break
        self.total_credit_hours -= course.credit_hours
        course.teacher = None

    def ListCourses(self):
        for course in self.courses:
            print(course)
            
    def DeliverLecture(self, course, date):
        lecture = Lecture(
            room = 107,
            course = course.name,
            teacher = self.name,
            hours = 3,
            date = date
        )
        if course.name in self.lectures.keys():
            self.lectures[course.name].append(lecture)
            course.AddLecture(lecture)
        else:
            self.lectures[course.name] = [lecture]
            course.AddLecture(lecture)
    
    def ListLectures(self, course):
        for lecture in self.lectures[course.name]:
            print(lecture)
