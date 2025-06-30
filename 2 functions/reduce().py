# basic example - function to add two numbers
from functools import reduce
def add(x, y):
    return x + y
a = [1, 2, 3, 4, 5]
res = reduce(add, a)
print(res)
# The reduce() function applies add() cumulatively to the elements in numbers.
#  First, 1 + 2 = 3. Then, 3 + 3 = 6.

# using reduce with lambda
from functools import reduce
a = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x + y, a)
print(res)

# using reduce with operator functions
import functools
import operator
a = [1, 3, 5, 6, 2]
print(functools.reduce(operator.add, a))
print(functools.reduce(operator.mul, a))
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

# difference btw reduce() and accumulate()
from itertools import accumulate
from operator import add
a = [1, 2, 3, 4, 5]
res = accumulate(a, add)
print(list(res))

# alternate of accumulate
from itertools import accumulate
a = [1, 2, 3, 4]
res  = accumulate(a)
print(list(res))