#!/bin/python3
class MyQueue(object):
    def __init__(self):
        self.lifo = []

    def peek(self):
        return self.lifo[0]

    def pop(self):
        self.lifo.remove(self.lifo[0])

    def put(self, value):
        self.lifo.append(value)

queue = MyQueue()
queue.put(15)
queue.put(17)
print(queue.peek())
queue.put(25)
print(queue.peek())
queue.pop()
print(queue.peek())
queue.pop()
print(queue.peek())






















