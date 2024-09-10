#1 sum of current number and previous number with fixed range

# previous_num = 0
# for current_num in range(10):
#     sum_num = current_num + previous_num
#     print(f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_num}")
#     previous_num = current_num




#2 Sum of current number and previous number with user defined range

def sumOfCurrentNumberAndPreviousNumber(start, end):
    for currentNum in range(start, end):
        previousSum = currentNum - 1
        sumu =  currentNum + previousSum
        print(f"Sum of {currentNum} and {previousSum}: ", sumu)

        previousSum = currentNum

start, end = map(int, input("Enter the range till sum you want: ").split(','))
sumOfCurrentNumberAndPreviousNumber(start, end)

