#1 check if first and last number are same or not in a single number


# def checkIfFirstAndLastNumAreSame(numi):
#     num = str(numi)
#     if len(num) == 1:
#         return False
#     if num[0] == num[-1]:
#         return True
    
# numi = int(input("Enter the number: "))
# print(checkIfFirstAndLastNumAreSame(numi))


#EXAMPLE 1
# Enter the number: 2
# False

# Enter the number: 19001
# True



#2 check if the first and last number in a my_list are same or not

# def definingList(n):
#     my_list = []
#     for i in range(n):
#         val = int(input(f"Enter {i} value to make a my_list: "))
#         my_list.append(val)
#     return my_list

# def firstAndLastNumberAreSameInList(my_list):
#     if len(my_list) <= 1:
#         return False
#     else:
#         if my_list[0] == my_list[-1]:
#             return True
#         else:
#             return False
    
# n = int(input("Enter the len of my_list: "))
# my_list = definingList(n)
# print(my_list)
# print(firstAndLastNumberAreSameInList(my_list))




#3 updated code to showcase python clarity, simplicity and readibility

def definingList(n):
    my_list = []  # Avoid using 'list' as a variable name
    for i in range(n):
        val = int(input(f"Enter value {i + 1} to make a list: "))  # User-friendly prompt {i changes to i + 1} 
        my_list.append(val)
    return my_list

def firstAndLastNumberAreSameInList(my_list):
    if len(my_list) <= 1:  # Handle cases with 0 or 1 element
        return False
    return my_list[0] == my_list[-1]  # Simplified return statement

n = int(input("Enter the length of the list: "))
my_list = definingList(n)  # Direct assignment
print(f"The list is: {my_list}")
print(f"First and last numbers are the same: {firstAndLastNumberAreSameInList(my_list)}")


# EXAMPLE 1
# Enter the length of the list: 4
# Enter value 1 to make a list: 4
# Enter value 2 to make a list: 2
# Enter value 3 to make a list: 3
# Enter value 4 to make a list: 4
# The list is: [4, 2, 3, 4]
# First and last numbers are the same: True

# EXAMPLE 2
# Enter the length of the list: 4
# Enter value 1 to make a list: 4
# Enter value 2 to make a list: 3
# Enter value 3 to make a list: 2
# Enter value 4 to make a list: 1
# The list is: [4, 3, 2, 1]
# First and last numbers are the same: False