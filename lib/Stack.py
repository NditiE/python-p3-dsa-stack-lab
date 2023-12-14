class Stack:
    def __init__(self, items=None, limit=None):
        self.limit = limit
        self.elements = items if items else []

    def push(self, item):
        if self.limit is None or len(self.elements) < self.limit:
            self.elements.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            raise IndexError("Pop from empty stack")

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return not bool(self.elements)

    def full(self):
        if self.limit is None:
            return False
        return len(self.elements) >= self.limit

    def search(self, value):
        if value in self.elements:
            return len(self.elements) - self.elements.index(value) - 1
        return -1
