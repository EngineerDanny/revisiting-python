

class Person :
    gender = 'Male'

    def __init__(self):
        print('Constructor called')
        pass
    

    # def __init__(self, name, age):
    #   self.name = name
    #   self.age = age




person = Person()
print(person.gender)
