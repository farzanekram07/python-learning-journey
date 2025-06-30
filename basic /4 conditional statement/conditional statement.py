#1. if conditional statement
age = 20
if age >= 18:
    print("Eligible to vote.")
# short-hand if
age = 19
if age > 18: print("Eligible to Vote.")


#2. if-else conditional statement
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
# short-hand if-else
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")


#3. elif statement
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


#4. nested if-else conditional statement
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


#5. ternary conditional statement
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)


#6. match-case statement
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")


