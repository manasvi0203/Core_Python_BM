# tuples

a = ()
print(type(a))

a = (1,2,3,4,)
b = 1,2
c = 1,
print("b is: ",type(b))
print("c is: ",type(c))

d = (1,2,3,4,5,6,7,8,9,10,11)

# indexing in tuples)
print(d[0])
print(d[-1])

# slicing in tuples
print(d[2:7:2])

print(d.count(1))

print(sum(d))

print(sorted(d, reverse=True))

# d[0] =2
# d.append(2)
