"""
Dictionaries
"""

family_members = {
    "father": "Ryan",
    "mother": "Ina",
    "daughter": "Arrum",
    "number_of_baby_sitter": 1
}

print(family_members.get("father"))
print(family_members.items())
print(family_members.keys())
family_members.popitem()
print(family_members)
family_members.setdefault("number_of_ex_baby_sitter", 5)
print(family_members)

new_family_members = {
    "son": "Maulana",
    "number_of_ex_baby_sitter": "10"
}

family_members.update(new_family_members)

print(family_members)

family_members.update(number_of_ex_baby_sitter=15)

print(family_members)
