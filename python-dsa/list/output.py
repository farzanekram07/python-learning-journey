# Output
# print list in python
#1. print
a = [1, 2, 3, 4, 5]
print(a)

#2. print with * operator
print(*a)
print(*a, sep = ',')

#3. using a loop
for num in a:
    print(num, end = ' ')

#4. using.join() - join list of strings
text = ['Welcome', 'Home', 'Farzan']
print(' '.join(text))

#5. using map() with .join() - join list of numbers
number = [1, 2, 3, 4, 5]
print(' '.join(map(str, number)))