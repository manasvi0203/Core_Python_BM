import time
start = time.time()
list1  = [100-i for i in range(100)]
print(list1)
for i in range(len(list1)):

    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print("Time Taken",time.time()-start)
print(list1)
