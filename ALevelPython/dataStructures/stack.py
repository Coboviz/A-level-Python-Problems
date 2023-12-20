# stack is a last in first out data structure
# we can't access elements of the stack by index, but
# rather we have to pop (take them off them stack) to
# see their values



#stack.append(1)
#stack.append(2)
#stack.append(3)
#stack.append(4)
#stack.pop()
#stack.append(5)
#print(stack)
# this is a normal way
# we are going to simulate it a bit different
# CAMBRIDGE!!

# We are going to create a stack which can hold up to 10 elements
# values are going to be x if it's an empty slot and that's it
# we are going to make it circular    5 6 7 8 9 10 1 2 3 4

stack = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']

bottomOfTheStack = 0
topOfTheStack = 0
avaliable = 10

def stackPush(val):
    global bottomOfTheStack
    global topOfTheStack
    global avaliable
    if avaliable != 0:
        stack[topOfTheStack] = val
        avaliable -= 1
        if topOfTheStack == 9:
            topOfTheStack = 0
        else:
            topOfTheStack = topOfTheStack + 1
    else:
        print("Stack is full")

def stackPop():
    global bottomOfTheStack
    global topOfTheStack
    global avaliable
    if avaliable == 10:
        print("Stack is empty")
    else:
        if (topOfTheStack == 0):
            stack[9] = 'x'
            topOfTheStack = 9
        else:
            stack[topOfTheStack-1] = 'x'
            topOfTheStack -= 1


stackPop()

