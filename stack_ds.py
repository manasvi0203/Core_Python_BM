'''
stack is implemted using a list
top: integer havingindex number of top element
'''

def is_empty(stack):
    if stack == []:
        return True
    else:
        return False

def push(stack, item):
    stack.append(item)
    top = len(stack) - 1

def pop(stack):
    if is_empty(stack):
        return "UNDER FLOW"
    else:
        item = stack.pop()
        if len(stack) == 0:
            top = None
        else:
            top = len(stack) - 1
    return item

def seek(stack):
    if is_empty(stack):
        return "UNDER FLOW"
    else:
        top = len(stack)- 1
        return stack[top]
    
def display(stack):
    if is_empty(stack):
        return "UNDER FLOW"
    else:
        top = len(stack) -1
        print(stack[top], "<-- top")
        for item in range(top-1,-1,-1):
            print(stack[item])

stack = []
top = None

while True:
    print("Stack Operations: ")
    print("1. Push","2. Pop", "3. Seek", "4. Display", "5. Exit")
    ch = int(input("Enter your choice: "))
    if ch==1:
        item = int(input("Enter element to be pushed: "))
        push(stack, item)
    elif ch==2:
        print(pop(stack))
    elif ch==3:
        print(seek(stack))
    elif ch==4:
        display(stack)
    elif ch==5:
        break
    else:
        print("Invalid Choice")
