'''
#Stack implementation of a Linked List

class LinkedStack:
    #Nested Class#################
    class Node:
        __slots__ = 'element', 'next'
        def __init__(self, element, next):
            self.element = element
            self.next = next

    ###############################
    def __init__(self):
        #Create an empty stack
        self.Head = None
        self.size = 0

    def push(self, e):
        self.Head = self.Node(e, self.Head)
        self.size += 1

    def pop(self):
        answer = self.Head.element
        self.Head = self.Head.next
        self.size -= 1
        return answer

    def readLinkedList(self, Current):
        while(Current.next!=None):
            print(Current.element)
            Current= Current.next
        print(Current.element)



LS = LinkedStack()
LS.push(34)
LS.push(90)
LS.push(40)
LS.push(60)
LS.readLinkedList(LS.Head)
print('Results after popping from the linked list')
LS.pop()
LS.readLinkedList(LS.Head)

'''

'''
#Queue implementation of a linked list

class LinkedQueue:
    class Node:
        __slots__ = 'element', 'next'
        def __init__(self, element, next):
            self.element = element
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
        self.queueLength = 0

    def push(self, e):
        if(self.queueLength == 0):
            #Enque them at back
            self.head = self.Node(e, None)
            self.tail = self.head
            self.queueLength += 1
        else:
            current = self.Node(e, None)
            self.tail.next = current
            self.tail = current
            self.queueLength += 1

    def pop(self):
        #Deque them from front
        if (self.queueLength == 0):
            print("Empty List")
        else:
            current = self.head.next
            self.head.element = None
            self.head = current
            self.queueLength -= 1
            if(self.queueLength==0):
                self.tail = None

    def readQueue(self, present):
            present = self.head
            while (present.next!= None):
                print(present.element)
                present = present.next
            print(present.element)
            print("Print Over")


LQ = LinkedQueue()
LQ.push(2)
LQ.push(4)
LQ.push(3)
LQ.readQueue(LQ.head)
LQ.pop()
LQ.readQueue(LQ.head)
LQ.push(6)
LQ.readQueue(LQ.head)
LQ.pop()
LQ.readQueue(LQ.head)
LQ.readQueue(LQ.head)

'''
'''
#Circular Queue/ Round Robin Scheduler

class CircularQueue:
    class Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.tail = None
        self.size = 0

    def enque(self, e):
        newest = self.Node(e, None)
        if(self.size == 0):
            newest.next = newest
            self.tail = newest
            self.size += 1
        else:
            newest.next = self.tail.next
            self.tail.next = newest
            self.tail = newest
            self.size += 1

    def deque(self):
            answer = self.tail.next.element
            if(self.size > 0):
                self.tail.next= self.tail.next.next
                self.size -= 1
            else:
                return print('List is empty')
            return answer

    def rotate(self):
        if (self.size > 0):
            self.tail = self.tail.next

LQ = CircularQueue()
LQ.enque(2)
LQ.enque(4)
LQ.enque(3)
print(LQ.deque())
LQ.rotate()
LQ.enque(6)
print(LQ.deque())
'''
#Doubly Linked List



























































