stack = []

bottomOfTheStack = 0
topOfTheStack = 0


def stackPush(val):
    global bottomOfTheStack
    global topOfTheStack
    stack.append(val)
    topOfTheStack += 1


def stackPop():
    global bottomOfTheStack
    global topOfTheStack
    if (bottomOfTheStack == topOfTheStack): # means stack is empty
        print("Nothing to pop, stack is empty")
    
    stack[topOfTheStack-1] = 'x'
    topOfTheStack -= 1


stackPush(1)
stackPush(1)
stackPush(1)
stackPush(1)
stackPush(1)
stackPush(1)
stackPop()
stackPop()
stackPop()

print(stack)
print(bottomOfTheStack)
print(topOfTheStack)
    