

class Singleton:

    _instance = None
    
    def __new__(cls, name, age):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self, name, age):
        self.name = name
        self.age = age


obj_1 = Singleton('Alice', 23)

obj_2 = Singleton('Bob', 27)

# print(obj_1 is obj_2)

# print(id(obj_1))
# print(id(obj_2))



def singleton(cls):

    instance = {}

    def inner(*args, **kwargs):

        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)

        return instance[cls]
    
    return inner


@singleton
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city



person_1 = Person('Emily', 24, 'Paris')
# person_2 = Person('Michael', 28, 'Berlin')
print(id(person_1))
print(person_1.city)

del person_1

import time
time.sleep(5)
# print(person_1 is person_2)

person_1 = Person('Emily', 20, 'Berlin')
print(id(person_1))

print(person_1.city)

# print(id(person_1))
# print(id(person_2))
# print(id(Person))
# print(id(singleton))


