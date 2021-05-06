'''num = int(input())

if num%2==1:
    print("Odd Number")
else:
    print("Even Number")'''

'''a = 34
b = 36
c = 56
# if condtion:
if a>b and a>c:
    print("a is larger")
elif b>c:
    print("b is larger")
else:
    print("c is a larger")'''

a = 23
b = 72
c = 78
print("a is larger") if a>b and a>c else print("b is larger") if b>c else print("c is largest")

## nested if-else

num = 23
if num%2==0:
    if num> 0 and num<10:
        print("Yes")
    else:
        print("Even number")
else:
    print("odd Number")
