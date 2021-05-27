import time
start = time.time()

arr = [100-i for i in range(100)]
print(arr)

for i in range(len(arr)):
    key = arr[i]
    j = i -1
    while j>=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key
print("time taken: ",time.time()-start)
print(arr)
