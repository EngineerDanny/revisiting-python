

class Person :
    gender = 'Male'
    
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def get_name(self):
      print("Called a function from an obj")
      return 'String'


person = Person("Danny" , 20)
print(person.age)

person.get_name()

