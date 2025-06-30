# every iterable DS use this - like list, tuple
# return map object
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))


#1. Converting map() object to a list
a = [1, 2, 3, 4]
def double(val):
  return val*2
res = list(map(double, a))
print(res)

# same problem solved using
# using list comprehension
def double(list):
  return [val * 2 for val in list]
a = [1, 2, 3, 4]
print(double(a))

# uisng lambda function
a = [1, 2, 3, 4]
double = lambda val: val * 2
res = list(map(double, a))
print(res)

# one liner lambda
a = [1, 2, 3, 4]
res = list(map(lambda x: x * 2, a))
print(res)


#2. using map() with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))



# recommended examples of map() function
#1. Converting to uppercase
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

#2. Extracting first character from strings
words = ['apple', 'banana', 'cherry']
res = map(lambda s: s[0], words)
print(list(res))

#3. Removing whitespaces from strings
s = ['  hello  ', '  world ', ' python  ']
res = map(lambda x: x.strip(), s)
print(list(res))

#4. Calculate fahrenheit from celsius
celsius = [0, 20, 37, 100]
res = list(map(lambda x: (x*9/5)+32, celsius))
print(res)