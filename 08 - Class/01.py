class First:
  x = 5

obj1 = First()
print(obj1)
print(obj1.x)

class Second:
  x = 6
  def speakTo(self, name):
    print("Hello "+name)

obj2 = Second()
obj2.speakTo("Alex")
