a = [1,2,3,2,31,1.22,"hello"]
print(a)
print(type(a))

print("element at zero position: ",a[0])
print("element at first position: ",a[1])

a.append("brain")
print(a)

a.extend(["mentors","coding",2,3])
print(a)

a.insert(1, "python")
print(a)

a[1] = "hello"
print(a)

a.append(["mentors","coding",2,3])
print(a)

item = a.pop()
print(item)
print(a)

a.remove("hello")
print(a)

print(a.count(2))

a.reverse()
print(a)

b = [1,34,51,16,27,8]
b.sort(reverse=True)
print(b)

print(sorted(b, reverse=True))

c = ["hello", "coding", "world"]
c.sort()
print(c)

d = ["1","hello","3", "good"]
d.sort()
print(d)
