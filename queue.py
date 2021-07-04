print("")
# ---------------- Queue-1 --------------------

queue1 = []

queue1.append("a")
queue1.append("b")
queue1.append("c")

print("QUEUE :  ", queue1)

queue1.pop(0)
print("After Dequeue-(i) :", queue1)
queue1.pop(0)
print("After Dequeue-(ii) :", queue1)
queue1.pop(0)
print("After Dequeue-(iii) :", queue1)


print("")

#---------------- Queue-2 --------------------


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print("QUEUE : ", self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
# inserting elements
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()
# removing an element
q.dequeue()

print("After removing an element")
q.display()


print("")



#---------------- Queue-3 --------------------



class Queue1:
    def __init__(self):
        self.queue1 = []

    def size1(self):
        print("Length of Queue :", len(self.queue1))

    def is_Empty(self):
        len(self.queue1) == 0

    def is_Full(self):
        return len(self.queue1) == self.size1

    def enqueue1(self, item1):
        if self.is_Full() != True:
            self.queue1.append(item1)
        else:
            print("Queue is full.")
        
    def dequeue1(self):
        if self.is_Empty() != True:
            self.queue1.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if len(self.queue1) == 0:
            print('Queue is Empty!')
        else:
            print("Peak element :", self.queue1[0])

    def display1(self):
        print("QUEUE : ", self.queue1)

myQueue = Queue1()
myQueue.enqueue1(4)
myQueue.enqueue1(5)
myQueue.enqueue1(6)
    
myQueue.display1()

myQueue.peek()

myQueue.dequeue1()
myQueue.dequeue1()

myQueue.display1()

myQueue.peek()

myQueue.display1()

myQueue.dequeue1()

myQueue.display1()

myQueue.is_Empty()
myQueue.size1()
myQueue.peek()

print("")


