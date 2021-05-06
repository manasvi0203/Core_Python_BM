## dictionary

a = {}

# dic keys should be either primitive datatype or tuple
dic = {"a":1,"b":[[1,2],[3,4]],"c":(4,5), 1:"2,3", (2,3):3}
print(dic)

print(dic["c"])
print(dic["b"])


print(dic.keys()) # returns keys in dic
print(dic.values()) # returns values in dic
print(dic.items()) # returns key, value pair in dic

dic["a"] = "hello"
print(dic)

dic["brain"]= "mentors"
print(dic)

d2 = {"d":3,"e":"f"}

dic.update(d2)
print(dic)
