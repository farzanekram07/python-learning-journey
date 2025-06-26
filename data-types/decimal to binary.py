# brute force
def decimal_to_binary1(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

# built-in function
def decimal_to_binary2(num):
    return bin(num)[2:]

num = int(input("Enter the number to get binary: "))
print("Brute force :", decimal_to_binary1(num))
print("Built-in :", decimal_to_binary2(num))