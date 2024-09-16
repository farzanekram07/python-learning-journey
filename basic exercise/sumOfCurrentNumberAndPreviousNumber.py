#1 sum of current number and previous number with fixed range

# previous_num = 0
# for current_num in range(10):
#     sum_num = current_num + previous_num
#     print(f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_num}")
#     previous_num = current_num




#2 Sum of current number and previous number with user defined range

def sumOfCurrentNumberAndPreviousNumber(start, end):
    for currentNum in range(start, end):
        previousNum = currentNum - 1
        sumu =  currentNum + previousNum
        print(f"Sum of {currentNum} and {previousNum}: ", sumu)

        previousNum = currentNum

start, end = map(int, input("Enter the range till sum you want: ").split(','))
sumOfCurrentNumberAndPreviousNumber(start, end)


#EXAMPLE
# Enter the range till sum you want: 4, 7
# Sum of 4 and 3:  7
# Sum of 5 and 4:  9
# Sum of 6 and 5:  11