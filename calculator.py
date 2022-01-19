def get_number():
    num1 = float(input("Please enter a number:"))
    return num1
def display(n):
    print(n)
    return
def calculate(n1,n2,operand):
    if operand == "+":
        s = n1+n2
    elif operand == "-":
        s = n1-n2
    elif operand == "*":
        s = n1*n2
    elif operand == "/":
        if n2 != 0:
            s = n1/n2
        else:
            return "Cannot divide by 0"
    return s

get_number()