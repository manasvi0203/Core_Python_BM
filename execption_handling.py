def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

try:
    num1 = int(input())
    num2 = int(input())
    op = input()
    dic = {"+":add, "-":subract,"*":multiply,"/":divide}
    res = dic[op](num1,num2)


except KeyError:
    print("Enter a valid operation")
except ZeroDivisionError:
    print("Division by zero not possible")
except ValueError:
    print("Please Enter valid Numbers")
except BaseException:
    print("Some Error")
else:
    print("Success")

    




    

