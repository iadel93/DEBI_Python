from student import Student
from course import Course
from teacher import Teacher




amr = Student(
    name = "Amr Ahmed",
    age = 18,
    major = "Engineering",
    level = "Senior",
    id = "std_1234"
)

print(amr)

math = Course(
    id = "mth_1234",
    name = "Math_1",
    credit_hours = 3
)

amr.Register(math)

print("Amr Courses:")
amr.ListCourses()

print("Math Students:")
math.ListStudents()


hany = Teacher(
    name = "Hany",
    id = "ta_1234",
    age = 30,
    salary = 5000,
    department = "Math"
)

hany.AddCourse(math)

print("Hany Courses:")
hany.ListCourses()

hany.DeliverLecture(math, "13-12-2024")

hany.ListLectures(math)
math.ListLectures()

amr.Attend(math, "13-12-2024")
