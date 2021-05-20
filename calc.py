def add(a,b):
    return a+b

def subract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd number: "))
op = input("Enter the operator: ")

dic = {"+":add, "-":subract, "*":multiply, "/":divide}

print(dic[op](num1, num2))
