from art import logo

import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2


operations = {"+": add,
 "-": subtract,
 "/": divide,
 "*": multiply}


def calculate():
    print(logo)
    
    num1 = float(input("What's the first number?: "))

    work = True
  
    for operator in operations:
        print(operator)

    while work:
        operation = input("Pick an operation: ")

        num2 = float(input("What's the second number?: "))

        result = operations[operation](n1=num1, n2=num2)
            
        print(f"{num1} {operation} {num2} = {result}")

        ask_user = input(f"Type 'y to continue calculating with {result} or type 'n' to exit: ").lower()
        if ask_user == 'y':
            num1 = result
        elif ask_user == 'n':
            work = False
            os.system('clear')
            calculate()

if __name__ == '__main__':
    calculate()
