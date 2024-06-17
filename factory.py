
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return 'Car is moving.'
    

class Bus(Vehicle):
    def move(self):
        return 'Bus is moving.'


class Train(Vehicle):
    def move(self):
        return 'Car is moving.' 
    

class Vehiclefactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


class Factory(Vehiclefactory):
    def create_vehicle(self, type):
        return start_factory(type)
    

# def start_factory(type):
#     if type == 'car':
#         return Car()
#     elif type == 'bus':
#         return Bus()
#     elif type == 'train':
#         return Train()
#     else:
#         return 'Sorry, we do not produce bikes.'


def start_factory(type):
    types = {'car': Car(), 'bus': Bus(), 'train': Train()}
    return types[type]


factory_1 = Factory()

# car_1 = factory_1.create_vehicle('car').move()
# bus_1 = factory_1.create_vehicle('bus').move()

print(factory_1.create_vehicle('car').move())
print(factory_1.create_vehicle('bus').move())

# print(car_1.move())
# print(bus_1.move())