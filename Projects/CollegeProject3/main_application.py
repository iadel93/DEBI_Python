from student import Student
from course import Course
from teacher import Teacher

amr = Student(
    name = "Amr adel",
    id = "st_1234",
    age = 18,
    gender = "Male",
)

print(amr)

math = Course(
    name = "Math_1",
    id = "mth_123",
)

amr.Register(math)

print("Amr Courses:")
amr.ListCourses()

amr.Drop(math)

print("Amr Courses:")
amr.ListCourses()


ahmed = Teacher(
    name = "Ahmed Hany",
    id = "ta_1234",
    age = 30,
    gender= "Male",
    salary=5000
)

ahmed.Teach(math)

print("Ahmed Courses:")
ahmed.ListCourses()

ahmed.DeliverLab(math, "12/12/2022")
ahmed.DeliverLecture(math, "13/12/2022")

amr.Attend(math, "12/12/2022")
amr.Attend(math, "13/12/2022")

print("Amr Lectures:")
amr.ListLectures()

print("Amr Labs:")
amr.ListLabs()