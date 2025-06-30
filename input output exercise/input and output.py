## Learning
#1. taking input in Python
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

#2. take Multiple Input in Python
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

#3. take Conditional Input from user in Python
# Prompting the user for input
age_input = input("Enter your age: ")

#4. converting the input to an integer
age = int(age_input)
# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")




## Recommended Problems
#1. print in python
a = input()
b = input()
separator = input()[0]
# Print with space
print(a + " " + b)
# Print without newline at the end
print(a + " " + b, end = "")
# Print with separator
print(a + separator + b)
# Print without space
print(a + b)

#2. multiple printing
text = input()
n = int(input())
# Write your code below that prints a n times
print(text * n)
# printing with removing trailing spaces at the end and at the start
print((text * n).strip()) #strip used to remove spaces

#3. typecasting - int str
a = input()
b = input()
c = input()
# Write your code below that prints a a times and b b times, seperated by c
print((a * int(a)) + c + (b * int(b)))

#4. input in python
# Take string input and print the string input
text = input()
print(text)
# Take integer input and add 10 to the integer input and print
number = int(input())
result = number + 10
print(result)
# Take floating-point input and multiply the float input by 10 and print
float_number = float(input())
float_result = float_number * 10
print(float_result)
