from Queue import Queue
from Stack import Stack

"""
Simple check that goes through and puts the list of names into both a 
Queue and a Stack and makes sure that they are popped off correctly.
YOU DO NOT NEED TO EDIT THIS.
This is proof of concept
"""


# Create the queue and stack
stack1 = Stack()
queue1 = Queue()


list_of_names = ["Taylor", "Luke", "EJ", "Josh", "Rachel", "Blake"]

for name in list_of_names:
    stack1.push(name)
    queue1.enqueue(name)

index = 0
llon = len(list_of_names) - 1

while True:
    if stack1.isEmpty() and queue1.isEmpty():
        break
    else:
        if not stack1.isEmpty():
            item = stack1.pop()
            print("Popped off stack: {0} = {1}".format(item, list_of_names[llon - index]))
        if not queue1.isEmpty():
            item = queue1.dequeue()
            print("Dequeued off queue: {0} =  {1}".format(item, list_of_names[index]))
    index += 1
