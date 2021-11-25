################## class nasledovanie ##################
class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(f"I am {self.name} and I am {self.age} years old")

  def speak(self):
    print("I donn't know what I say")

class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color

  def speak(self):
    print("Meow")

  def show(self):
    print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
    
class Wolf(Pet):
  def speak(self):
    print("Bark")

p = Pet("Sherlock", 1)
p.show()
p.speak()
c = Cat("Murka", 5, "blue")
c.show()
c.speak()
d = Wolf("Chip", 25)
d.show()
d.speak()
