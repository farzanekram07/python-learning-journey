#1 using built-in function - count()

# def numOfOccurenceOfSubstringInAString(string):
#     str = string.count("Name")
#     return str

# string = "My Name is Farzan and My home Name is Kaify"
# print("substring name occured:", numOfOccurenceOfSubstringInAString(string), "times")


# EXAMPLE
# substring name occured: 2 times



#2 brute force

# def numOfOccurenceOfSubstringInAList(mainString, subString):
#     mainLength = len(mainString)
#     subLength = len(subString)
#     print("mainString:", mainString)
#     print("subString:", subString)
#     print("size of both string:", mainLength, subLength)

#     count = 0
#     for i in range(mainLength - subLength + 1):   #defining the range till loop runs
#         if mainString[i: i + len(subString)] == subString:  #slicing for checking or matching 
#             count = count + 1
#     return count

# mainString = "My name is farzan and my ign name is hakurrrpunk"
# subString = "name"
# print("number of times substring found:", numOfOccurenceOfSubstringInAList(mainString, subString))


# EXAMPLE
# mainString: My name is farzan and my ign name is hakurrrpunk
# subString: name
# size of both string: 48 4
# number of times substring found: 2



#3 optimized using hashset/dictionary

# def findNumberOfOccurenceOfSubstringInAList(mainString, subString):
#     hashset = {}
#     count = 0

#     for i in range(len(mainString) - len(subString) + 1):
#         curr_subString = mainString[i:i + len(subString)]

#         if curr_subString not in hashset:
#             hashset[curr_subString] = 0

#         if curr_subString == subString:
#             count = count + 1
    
#     return count

# mainString = "My name is farzan and my ign name is hakurrrpunk"
# subString = "name"
# print("number of times substring found:", findNumberOfOccurenceOfSubstringInAList(mainString, subString))


# EXAMPLE
# number of times substring found: 2


#4 using split + for loop
def findNumberOfOccurenceOfSubstringInAList(main_string, substring):
    parts = main_string.split(substring)
    return len(parts) - 1

mainString = "My name is farzan and my ign name is hakurrrpunk"
subString = "name"
print("number of times substring found:", findNumberOfOccurenceOfSubstringInAList(mainString, subString))


# EXAMPLE
# number of times substring found: 2