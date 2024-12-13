class Person():
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id

    def __str__(self):
        return f"{self.name}"

class Student(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age,id)
        self.grade = -1
        self.courses = []

    def register(self,course):
        course.add_student(self)
        self.courses.append(course)

    def drop(self,course):
        course.drop_student(self)
        for i in range(len(self.courses)):
            if self.courses[i].course_name == course.course_name:
                self.courses.pop(i)
                break

    def attend(self,course,date):
        course.student_attend(self,date)

    def list_courses_grades(self):
        for course in self.courses:
            try:
                print(f"{course.course_name} : {course.student_grades[self.id]}")
            except:
                print(f"{course.course_name} : It has no grade yet")








class Teacher(Person):
    def __init__(self,name,age,id, salary):
        super().__init__(name,age,id)
        self.courses = []
        self.salary = salary

    def Register(self,course):
        self.courses.append(course)

    def register(self,course):
        course.add_teacher(self)
        self.courses.append(course)

    def drop(self,course):
        course.drop_teacher(self)
        for i in range(len(self.courses)):
            if self.courses[i].course_name == course.course_name:
                self.courses.pop(i)
                break

    def assess(self,student,grade,course):
        course.add_grade(student,grade)


    def attend(self,course,date):
        course.deliver_lecture(date,self)






class Course():
    def __init__(self,id,name,credit,teacher):
        self.course_id = id
        self.course_name = name
        self.course_credit = credit
        self.course_teacher = teacher
        self.students = []
        self.teachers = []
        self.lectures = {}
        self.student_attendance = {}   
        self.student_grades = {}
        

    def add_student(self,student):
        self.students.append(student)

    def drop_student(self,student):
        self.students.remove(student)

    def add_teacher(self,teacher):
        self.course_teacher = teacher

    def drop_teacher(self,teacher):
        self.course_teacher = None

    def deliver_lecture(self,lecture_date,teacher):
        self.lectures[lecture_date] = teacher
        self.student_attendance[lecture_date] = []

    def student_attend(self,student,lecture_date):
        self.student_attendance[lecture_date].append(student)

    def add_grade(self,student,grade):
        self.student_grades[student.id] = grade




    def __str__(self):
        return f"{self.course_name}"



    