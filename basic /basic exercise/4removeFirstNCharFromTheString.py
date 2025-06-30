def removeFirstNCharacterFromTheString(str, m):
    return str[m:]

str = input("Enter the String: ")
m = int(input("Enter the N character you want to remove: "))
print(removeFirstNCharacterFromTheString(str, m))


#EXAMPLE
# Enter the String: MynameisFarzan
# Enter the N character you want to remove: 2
# Output : nameisFarzan