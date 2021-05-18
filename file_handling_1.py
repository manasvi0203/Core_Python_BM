# read requires a file
# read, readlines, readline
'''file = open("whyw.txt", "r")
data = file.readline()
data_1  = file.readlines()
file.close()
print(data)
print(data_1)'''


'''file = open("first_write_file.txt","w")
data = "The content has been changed"
file.write(data)
print(data)
file.close()'''

file = open("first_write_file.txt","a")
data = "Adding something else to file"
file.write(data)
print(data)
file.close()


