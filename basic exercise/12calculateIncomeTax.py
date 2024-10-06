def incomeTax(income):
    tax = 0
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        x = (income - 10000)
        tax = (x * 10) / 100 
    else:
        tax = 0     #first 10000
        tax = (10000 * 10) / 100    #second 10000
        tax += ((45000 - 20000) * 20) / 100   #remaining 25000
        

    return tax

income = 25000
print(incomeTax(income))


