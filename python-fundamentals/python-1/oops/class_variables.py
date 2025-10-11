class Student:

    class_year = 2025
    num_students = 0
    

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("John", 30)
student2 = Student("Jenny", 23)
student3 = Student("David", 28)
student4 = Student("Sandy", 26)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)


# print(Student.num_students)

# print(student2.name)
# print(student2.age)
# print(Student.class_year)