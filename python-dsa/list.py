# User input in a List
#1. Get a list as input from user in Python
# Get user input and split it into a list
user_input = input("Enter elements separated by space: ").split()
print("List:", user_input)

#2. Get a list of integers, using list comprehension
user_input1 = list(map(int, input("Enter the elements separated by space: ").split()))
print("List of integers: ", user_input1)

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



# Multi-Dimensional List
str = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
print("string to flatten:", str)
# make a single list using loop
flatten = []
for list in str:
    for item in list:
        flatten.append(item)
print("flatten using loop:", flatten)

# make a single list using list comprehension
flattern = [item for list in str for item in list]
print("flatten using list comprehension:", flattern)

# convert list into space separated stirng
string = ' '.join(flattern)
print(string)
type(string)

# remove spaces from that string
string1 = ''.join(flattern)
print(string1)