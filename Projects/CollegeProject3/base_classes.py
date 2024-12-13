class Person():
    def __init__(self, name, id, age, gender):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name
        # return f"Name: {self.name}\nID: {self.id}\nAge: {self.age}\nGender: {self.gender}"


class Session():
    def __init__(self, date, type, course_name, teacher, building):
        self.date = date
        self.type = type
        self.course_name = course_name
        self.teacher = teacher
        self.building = building
        self.attended_students = []

    def Attend(self, student):
        self.attended_students.append(student)

    def __str__(self):
        return f"Date: {self.date}\nType: {self.type}\nCourse Name: {self.course_name}"