# class variables = shared among all of the class, defined outside the constructor, allow you to share data among all objects created from that class

class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("John", 23)
student2 = Student("David", 30)
student3 = Student("Jenny", 26)
student4 = Student("Sandy", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

