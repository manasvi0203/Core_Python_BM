# break and continue statement
'''
for i in range(20):
    print("inside loop") 
    if i==13:
        # it stops the loop
        break
print("outide loop")
'''

for i in range(20):
    if i == 13:
        continue
    print(i)
print("outside loop")
