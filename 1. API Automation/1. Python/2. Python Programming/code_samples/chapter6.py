"""
Lists
"""

family_members = ["Ryan", "Ina", "Arrum"]
baby_sitters = ["Wiwi", "Siti"]

print(family_members)
print(baby_sitters)

baby_sitters.append("Ema")

print(baby_sitters)

family_members.extend(baby_sitters)

print(family_members)

family_members.remove("Wiwi")

print(family_members)

family_members.pop(-2)

print(family_members)

family_members.sort()

print(family_members)

print("Arrum" in family_members)

print(family_members.count('Arrum'))

print(family_members.index('Arrum'))
