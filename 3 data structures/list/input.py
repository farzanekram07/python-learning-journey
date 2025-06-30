# User input in a List
#1. Get a list as input from user in Python
# Get user input and split it into a list
user_input = input("Enter elements separated by space: ").split()
print("List:", user_input)

#2. Get a list of integers, using list comprehension
user_input1 = list(map(int, input("Enter the elements separated by space: ").split()))
print("List of  integers: ", user_input1)