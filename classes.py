class Person:
    number_of_students = 0
    graduation = 1
    def __init__(student, name, age, grade):
        student.name = name
        student.age = age
        student.grade = grade
        Person.number_of_students += 1

    def graduation_class(student):
        student.grade = int(student.grade + student.graduation)

    def email(student):
        return f"{student.name}@gmail.com"

    def __str__(student):
        return f"{student.name} {student.age} {student.grade} {student.email()}"


p1 = Person("John", 36, 5)

print(Person.number_of_students)
p1.graduation_class()
print(p1.grade)
print(p1.__dict__)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#
# p1 = Person("John", 36)
#
# print(p1.name, p1.age)