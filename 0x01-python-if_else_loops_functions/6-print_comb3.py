#!/usr/bin/python3
for x in range(9):
    for y in range(1, 9 +1):
        if x >= y :
            continue
        if x == 8:
            print("{:d}{:d}".format(x,y),end="")
            print()
            break
        else:
            print("{:d}{:d}".format(x,y),end=", ")
