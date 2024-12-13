class Person():
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def __str__(self):
        return self.name


class Lecture():
    def __init__(self, room, course, teacher, hours, date):
        self.room = room
        self.course = course
        self.teacher = teacher
        self.hours = hours
        self.date = date
        self.attendant_students=[]

    def Attend(self, student):
        self.attendant_students.append(student)

    def __str__(self):
        return f"{self.course}_{self.date}"