class Course():

    def __init__(self, name, id):

        self.name = name
        self.id = id
        self.students = []
        self.teacher = None
        self.lectures = []
        self.labs = []

    def AddStudent(self, student):
        self.students.append(student)
    
    def RemoveStudent(self, student):
        for i in range(len(self.students)):
            if self.students[i].id == student.id:
                self.students.pop(i)
                break

    def AddTeacher(self, teacher):
        self.teacher = teacher
    
    def RemoveTeacher(self):
        self.teacher = None

    def DeliverLecture(self, lecture):
        self.lectures.append(lecture)

    def DeliverLab(self, lab):
        self.labs.append(lab)
    
    def AttendStudent(self, student, date):
        done = False
        for lecture in self.lectures:
            if lecture.date == date:
                lecture.Attend(student)
                done = True
                return lecture
        
        for lab in self.labs:
            if lab.date == date:
                lab.Attend(student)
                done = True
                return lab
            
        if not done:
            print("Date not found")
            return None
        

    def __str__(self):
        return self.name



    