'''def myfun():
    print("First Function")

print("This Statments prints something")
myfun()
print("This Statments prints something else") 
myfun()
print("Another print statment")
myfun()'''

# parametrized functions
'''def add(a,b):

    print(a+b)

def subract(a,b):

    print(a-b)

def multiplication(a,b):

    print(a*b)

def divide(a,b):

    print(a/b)

c = int(input("Enter first Number: "))
d = int(input("Enter second number: "))

add(c,d)
subract(c,d)
multiplication(c,d)
divide(c,d)'''

'''def calc(a,b):
    print(a)
    print(b)
    print(a+b,a-b,a*b,a/b)

calc(b=30, a=40)'''

'''def sum_list(a):
    print(sum(a))
a = [1,2,3,4,5,6]

sum_list(a)'''

def prime_num(num):
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            print("Not Prime")
            break
    else:
        print("Prime Number")

prime_num(int(input("Enter one Number: ")))
           


