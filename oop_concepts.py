# a, e, i, p


class Vehicle:

    bmw = 'One of the most popular car brands in the world.'

    _mercedes = 'Another popular luxary car brand.'

    __remote_key = 'pasSworD5485'

    # instance method
    def move(self):
        speed = 145
        return speed
    
    def stop(self):
        return 'The vehicle has stopped.'
    
    @classmethod
    def fuel(cls):
        return 'Fill up tank every 7 days.'
    
    @staticmethod
    def brake():
        return 'Brake the vehicle when the traffic light is red.'


obj_1 = Vehicle()

# print(obj_1.fuel())
# print(Vehicle.fuel())

print(obj_1.brake())



class Railtrack:
    pass
    

class Train(Vehicle, Railtrack):
    
    def route(self):
        return 'From Berlin to Paris.'





# obj_2 = Train()

# print(obj_2.route())
# print(obj_2.move())

# print(obj_1.bmw)

# print(obj_1._mercedes)


# print(obj_1.__remote_key)

# print(obj_1.move())

# print(Vehicle.move())



