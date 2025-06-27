class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        #code here
        match operator:
            case 1:
                print(a + b, end = "")
            case 2:
                print(b - a, end = "")
            case 3:
                print(a * b, end = "")
            case _:
                print("Invalid Input", end = "")