import sys

def add(num1, num2):
    a = num1 + num2
    return a

def sub(num1, num2):
    s = num1 - num2
    return s

def mul(num1, num2):
    m = num1 * num2
    return m

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operator = sys.argv[3]


if operator == "+":
    print("Result:",add(num1, num2))

elif operator == "-":
    print("Result:",sub(num1, num2))

elif operator == "*":
    print("Result:",mul(num1, num2))

else: print("Invalid operator")