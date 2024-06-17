
from abc import ABC, abstractmethod


class Software(ABC):
    
    version = 'v1.0'

    @abstractmethod
    def add_feature(self):
        pass


class MeetingSoftware(Software):

    __product_key = 'DJKSE-DFJS93-DFJKD94JD-DJKD94JD'
    
    def add_feature(self):
        return 'Access camera of the device.'
    
    
    @property
    def activate_key(self):
        return self.__product_key
    
    @activate_key.setter
    def activate_key(self, value):
        self.__product_key = value



# m1 = MeetingSoftware()

# print(m1.__product_key)

# print(m1.activate_key)


# m1.set_activate_key('FCMXC-RDWMP-RFGVD-8TGPD-VQQ2X')

# m1.activate_key = '4HNBK-863MH-6CR6P-GQ6WP-J42C9'

# print(m1.activate_key)


# print(m1.version)
# print(m1.add_feature())
        



class MobileTech:

    def __init__(self, brand, model, ram):
        self.brand = brand
        self.model = model
        self.ram = ram

        self.increased_ram = self.ram + 4


        print('We provide technology for mobile devices.')

    def display_type(self):
        return 'Devices with IPS display.'


class Smartphone(MobileTech):

    def __init__(self, brand, model, ram, memory, camera):

        super().__init__(brand, model, ram)
        self.memory = memory
        self.camera = camera

        print('The flagship phone from Samsung with AI feature.')
        print(super().display_type())
        print(super().display_type())
        print(super().display_type())
        print(super().display_type())

    def display_type(self):
        print('new method defined here.')
        print(super().display_type())
        return 'Devices with Amoled display.'




# p1 = MobileTech('Apple', 'iphone 15 pro', 6)

p2 = Smartphone('Samsung', 'Galaxy S23', 8, 256, 48)

print(p2.display_type())

# print(p2.camera)


# print(p1.increased_ram)

# p1.__init__()

