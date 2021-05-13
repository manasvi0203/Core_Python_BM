# list comprehension
# a must have values till 100
'''a= []
for i  in range(100):
    a.append(i)'''

a = [i for i in range(100)]
print(a)

b = [100 for i in range(100)]
print(b)

c = [i for i in range(100) if i%2==0]
print(c)

d = [[i for i in range(100) if i%2==0], [i for i in range(100) if i%2!=0]]
print(d)


