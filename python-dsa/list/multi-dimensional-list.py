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