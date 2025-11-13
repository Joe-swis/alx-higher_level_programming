#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
mod = number % 10 if number > 10 else number % -10
print("Last digit of {:d} is "
      .format(number),end="")
if mod > 5:
    print("{:d} and is greater than 5".format(mod))
elif mod == 0:
    print("{:d} and is 0".format(mod))
else:
    print("{:d} and is less than 6 and not 0".format(mod))
