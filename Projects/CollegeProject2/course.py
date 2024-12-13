class Course():

    def __init__(self, name, id, credit_hours):

        self.name = name
        self.id = id
        self.credit_hours = credit_hours
        self.students = []
        self.students_grades = {}
        self.teacher = None
        self.content = {}
        self.lectures = []

    def RegisterStudent(self, student):
        self.students.append(student)

    def DropStudent(self, student):
        for i in range(len(self.students)):
            if self.students[i].id == student.id:
                self.students.pop(i)
                break
    
    def ListStudents(self):
        for student in self.students:
            print(student)

    def AddLecture(self, lecture):
        self.lectures.append(lecture)

    def StudentAttendance(self, student, date):
        done  = False
        for lecture in self.lectures:
            if lecture.date == date:
                lecture.Attend(student)
                done = True

        if not done:
            print("Date is not found")

    def ListLectures(self):
        for lecture in self.lectures:
            print(lecture)



    def __str__(self):
        return self.name