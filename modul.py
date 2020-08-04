# Yöntem 1

# import math

# value = dir(math)
# value = help(math)
# value = help(math.sqrt)

# Yöntem 2
# from math import *

# value2 = sqrt(64)
# print(value2)

import random


result = int(random.uniform(1, 100))
result2 = random.randint(1, 100)

print(result)
print(result2)

import inheritance

kisi = inheritance.Person('furkan', 'aktas', 21)

print(kisi.last_name)

    #  PYTHON LIST COMPREHENSIONS

numbers = [x*x for x in range(10) if x%3 == 0]

print(numbers)
