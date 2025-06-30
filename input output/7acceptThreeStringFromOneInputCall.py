def threeInputFromOneInput():
    var = input().split()
    for i in range(3):
        print(f"name{i+1}:", var[i])
        

threeInputFromOneInput()

# str1, str2, str3 = input("Enter three string").split()
# print('Name1:', str1)
# print('Name2:', str2)
# print('Name3:', str3)