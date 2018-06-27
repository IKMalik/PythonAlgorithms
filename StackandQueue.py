#array implementation of stack

class Stack():

    def __init__(self):
        self.array_vals = []

    def push(self, value):
        self.array_vals.append(value)

    def pop(self):
        self.array_vals.pop()


class Queue():

    def __init__(self):
        self.list_vals = []

    def enqueue(self, value):
        self.list_vals.append(value)

    def dequeue(self):
        self.list_vals.pop(0)
        print(str(self.list_vals))
