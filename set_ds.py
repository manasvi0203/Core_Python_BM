s = {1,2,3,4,4,4,4,4,2,1,2,3,4,5,5,6,56,3,5,2,4,86,45}
s1 = {1,2,3,4,5,6,34,7,88,45,45,35,3,5,24,4,9}
print(type(s))
print(s)


print("result of intersection: ",s.intersection(s1))
print("result of intersection: ",s.union(s1))

print("s-s1: ",s - s1)
print("s1-s: ",s1 - s)
s2 = {1,2,3,4,5,6,34,7,88}
print(s.issuperset(s2))
print(s.issubset(s1))


