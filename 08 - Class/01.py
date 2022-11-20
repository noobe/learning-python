class First:
  x = 5

obj1 = First()
print(obj1)
print(obj1.x)

class Second:
  name = "Alex"
  def speakUp(self):
    print("Hello, I'm "+self.name)

obj2 = Second()
obj2.speakUp()

class Third:
  x = 6
  def speakTo(self, name):
    print("Hello "+name)

obj3 = Third()
obj3.speakTo("Alex")

class Fourth:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def speakUp(self):
    print("Hi, I'm "+self.name+" and I'm "+self.age+" years old.")

obj4 = Fourth("Jeb", "25")
obj4.speakUp();
print(obj4)

class Fifth:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"

obj5 = Fifth("Jeb", "25")
print(obj5)