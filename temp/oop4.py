################## class classmethod ##################
class Person:
  number_of_people = 0
  GRAVI = -9.8

  def __init__(self, name):
    self.name = name
    Person.add_person()

  @classmethod
  def number_of_people_(cls):
    return cls.number_of_people

  @classmethod
  def add_person(cls):
    cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people_())

# Person.number_of_people = 8
# print(p1.number_of_people)
# Person.number_of_people = 10
# print(p2.number_of_people)

################## class staticmethod ##################
class Math:

  @staticmethod
  def add5(x):
    return x + 5

print(Math.add5(6))
