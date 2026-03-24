from random import *

print(random()) # 0.0 <= x < 1.0
print(randint(2,20)) # 2 <= x <= 20
print(choice(['apple', 'banana', 'cherry'])) # randomly selects one of the items from sequence/string
print(uniform(1.5, 3.5)) # 1.5 <= x < 3.5
print(randrange(1, 10, 2)) # randomly selects an odd number between 1 and 10 (1, 3, 5, 7, or 9)
print(shuffle([1, 2, 3, 4, 5])) # randomly shuffles the list/tuple in place