#queue is a first in first out structure

queue = ['x', 'x', 'x', 'x', 'x', 
         'x', 'x', 'x', 'x', 'x',
         'x', 'x', 'x', 'x', 'x',
         'x', 'x', 'x', 'x', 'x',
         'x', 'x', 'x', 'x', 'x',
         'x', 'x', 'x', 'x', 'x']

frontOfTheQueue = 14
backOfTheQueue = 14

def enterQueue(val):
    global backOfTheQueue
    global frontOfTheQueue
    queue[backOfTheQueue]  = val
    backOfTheQueue = backOfTheQueue - 1

def leaveQueue():
    global backOfTheQueue
    global frontOfTheQueue
    if frontOfTheQueue != backOfTheQueue:
        queue[frontOfTheQueue] = 'x'
    else:
        print("queue is empty")


leaveQueue()

print(queue)



