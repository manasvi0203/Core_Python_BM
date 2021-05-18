'''def add(name, *c):
    print("hello",name)
    sum_1 = 0
    print(c)
    for value in c:
    
        sum_1 = sum_1 + value
    return sum_1

print(add("Gautam", 23,45,78, 12))'''

# eval

# input --> string format

'''a = input()
print(type(a))

b = eval(a)
print(b)
print(type(b))'''


def calc(a,b,op):
    def add():
        return a+b
    def subtract():
        return a-b
    if op=="+":
        return add()
    else:
        return subtract()

print(calc(23,45,"-"))



