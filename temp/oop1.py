################## class Dog ##################

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.age

  def set_age(self, age):
    self.age = age

  def bark(self):
    print("bark")
  
  def add_one(self, x):
    return x + 1

d = Dog("Tim", 5)
d.set_age(6)
print(d.get_name(), d.get_age())

d2 = Dog("Bill", 10)
print(d2.get_name(), d2.get_age())
# print(d2.get_age())
# d.bark()
# print(d.add_one(5))
