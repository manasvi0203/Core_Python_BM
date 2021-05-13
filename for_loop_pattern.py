'''
1111
2  2
3  3
4444
'''

n = 5
for i in range(1,n): # for rows
    if i==1 or i==n-1:
        print(str(i)*4)
    else:
        for j in range(1,n): # for columns
            if j==1 or j==n-1:
                print(str(i), end="  ")
        print()
