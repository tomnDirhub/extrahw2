from random import *
from time import time
seed(time())

first_stone = randint(3, 20)
result = ''
for i in range(1, first_stone - 1):
    for j in range(i + 1, first_stone):
        if first_stone % (i + j) == 0:
            result += str(i) + str(j)
print(first_stone)
print(result)