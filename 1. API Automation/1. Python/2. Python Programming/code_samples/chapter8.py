"""
Classes
"""


class FamilyMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print("Hello, my name is {}, and I am a/an {}".format(self.name, self.role))


ryan = FamilyMember("Ryan", "Father")
ryan.introduce()
