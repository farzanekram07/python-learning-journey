def printCharAtEvenIndex(str):
    for i in range(len(str)):
        if i % 2 == 0:
            print(str[i], end = " ")
    print()
str = input("Enter the string: ")
printCharAtEvenIndex(str) 


#EXAMPLE
# Input  : MYNAMEISFARZAN!!
# Output : M N M I F R A !  