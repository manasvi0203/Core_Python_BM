'''a = input("Enter any number: ")
print(type(a))

# string

a = float(input("Enter any number: "))
print(type(a))'''

'''
# adding two numbers
num1 = int(input())
num2 = int(input())
print(num1+num2)'''

'''num = input("Enter two numbers: ").split()
print(int(num[0]) + int(num[1]))'''
'''
num = list(map(int, input("Enter numbers: ").split()))
print(sum(num))'''
           
a = input() # user enters the number
a = a.split() # nunbers get splitted based on space and are stored as list
a = list(map(int, a)) # returns list of integer elements based on elements in list

print(sum(a))

