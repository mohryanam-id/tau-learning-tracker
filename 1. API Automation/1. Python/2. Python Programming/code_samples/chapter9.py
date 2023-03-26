"""
Inheritance and Polymorphism
"""
from chapter8 import FamilyMember


class Education:
    def __init__(self, latest_education):
        self.latest_education = latest_education

    def get_latest_education(self):
        return self.get_latest_education()

    def inform_latest_eduction(self):
        print('My latest education is: {}'.format(self.latest_education))


class Daughter(FamilyMember):
    def __init__(self, name):
        super().__init__(name, 'Daughter')


class Mother(FamilyMember):
    def __init__(self, name):
        super().__init__(name, 'Mother')


class Father(FamilyMember, Education):
    def __init__(self, name):
        FamilyMember.__init__(self, name, 'Father')
        Education.__init__(self, 'Sarjana')


class BabySitter(FamilyMember):
    def __int__(self, name):
        super().__init__(name, 'Test')

    def introduce(self):
        print('My name is {}, I love being part of the family'.format(self.name))


arrum = Daughter('Arrum')
arrum.introduce()

ina = Mother('ina')
ina.introduce()

ryan = Father('Ryan')
ryan.introduce()
ryan.inform_latest_eduction()

bi_ema = BabySitter('Bi Ema', 'Test')
bi_ema.introduce()
