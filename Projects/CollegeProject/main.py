from entities import Student,Course,Teacher

#### Trial 1 ####
available_courses = []
math = Course(id = "mth_123",
                name = "Math_1",
                credit = 3,
                teacher = "Ahmed")

available_courses.append(math)
print("####Available Courses####")
for course in available_courses:
    print(course)
# print(math)

hossam = Student("Hossam",18,"st_1234")
hossam.register(math)
print("##Registerd Courses##")
for course in hossam.courses:
    print(course)
print("##Students##")
for student in math.students:
    print(student)

hossam.drop(math)
print(hossam.courses)
print(math.students)

## Trial 2

ahmed = Teacher("Ahmed",30,"ta_1234",3000)
print(ahmed)

ahmed.register(math)
print("##Registerd Courses##")
for course in ahmed.courses:
    print(course)
print("##Teachers##")
print(math.course_teacher)


ahmed.attend(math,"5-12-2024")
print("##lectures Available##")
for lecture in math.lectures:
    print(lecture)

hossam.attend(math,"5-12-2024")
print("##Attendance##")
print(math.student_attendance)
print(math.student_attendance["5-12-2024"][0])

#### Trial 3
math_2 = Course(id = "mth_1212",
                name = "Math_2",
                credit = 3,
                teacher = "Ahmed")

hossam.register(math)
hossam.register(math_2)

ahmed.assess(hossam,50,math)
# ahmed.assess(hossam,70,math_2)

print("##Grades##")
print(math.student_grades)
print(math_2.student_grades)


print("## Student Grades ##")
hossam.list_courses_grades()

