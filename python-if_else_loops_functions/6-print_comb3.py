#!/usr/bin/python3
for i in range(0, 10):
    for i2 in range(i + 1, 10):
        if i == 8 and i2 == 9:
            print("{}{}".format(i, i2), end="")
        else:
            print("{}{}".format(i, i2), end=", " if i < 89 else "\n")
print("")
