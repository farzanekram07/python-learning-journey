#1. creation of string
s1 = 'GfG'
s2 = "GfG"
print(s1)
print(s2)

#2. multi-line string
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)
s = '''I'm a 
Geek'''
print(s)

#3. accessing characters of string
s = "GeeksforGeeks"
print(s[0])  
print(s[4])

#4. access string with negative indexing
s = "GeeksforGeeks"
print(s[-10])  
print(s[-5])

#5. string slicing
s = "GeeksforGeeks"
# Retrieves characters from index 1 to 3: 'eek'
print(s[1:4])  
# Retrieves characters from beginning to index 2: 'Gee'
print(s[:3])   
# Retrieves characters from index 3 to the end: 'ksforGeeks'
print(s[3:])   
# Reverse a string
print(s[::-1])

#6. string immutability
'''Strings in Python are immutable.  
If we need to manipulate strings then we can use methods 
like concatenation, slicing, or formatting.'''

s = "geeksforGeeks"
# create a new string to change its first character
s = "G" + s[1:]
print(s)

#7. deleting a string
s = "GfG"
del s

#8. updating a string
s = "hello geeks"
s1 = "H" + s[1:]
print(s1)

#9. common string methods
# len()
s = "GeeksforGeeks"
print(len(s))

# upper() and lower()
s = "Hello World"
print(s.upper())  
print(s.lower())

# strip()
s = "   Gfg   "
print(s.strip())    
s = "Python is fun"

# replace 'fun' with 'awesome'
print(s.replace("fun", "awesome"))
