# loops

# start, stop, step
'''for i in range(2,10,2):
    print(i)'''

'''
*
* *
* * *
* * * *
'''
for i in range(1,5):
    print("* "*i)

'''
1
2 2
3 3 3
4 4 4 4
'''

for i in range(1,5):
    print(str(i) * i)

'''
   *
  **
 ***
****
'''
n = 5
for i in range(1,n):
    print(" "*(n-i-1)+"*"*i)

'''
  *
 ***
*****
'''
# odd number (2*i - 1)
# n-i-1

for i in range(1,4):
    print(" "*(n-i-2)+"*"*(2*i-1))
'''
1111
2  2
3  3
4444
''' 

