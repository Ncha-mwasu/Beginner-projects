class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def email(self):
        return (f"{self.name}@gmail.com")


p1 = Person("John", 36)

print(p1.email())


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#
# p1 = Person("John", 36)
#
# print(p1.name, p1.age)