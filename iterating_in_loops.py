'''a = ["hello","world",1,2,34,True]

for item in a:
    print(item)

b = ("hello","world",1,2,34,True)
for item in b:
    print(item)'''

dic = {"a":1,"b":2,"c":3,"d":4}
print(dic.keys())
print(dic.values())
print(dic.items())


'''for a in dic.items():
    if a[1] == 4: # value whose key has to be returned
        print(a[0])
        break
'''

for i in range(len(dic)): 
    if list(dic.values())[i] == 3:
        print(list(dic.keys())[i])
        break


