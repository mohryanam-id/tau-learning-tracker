"""
loops
"""

names = ["Ryan", "Ina", "Arrum"]

for name in names:
    print("Family Member: {}".format(name))

for i in range(1, 11):
    print("Number: {}".format(i))

i = 1
while i < 11:
    print("Number: {}".format(i))
    i += 1

for i in range(1, 11):
    if i == 1:
        continue
    elif i == 2:
        pass
    elif i == 5:
        break
    print("Number: {}".format(i))