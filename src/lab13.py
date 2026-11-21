class Queue:
    def __init__(self):
        self._items = []
        self._head = 0

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._items[self._head]
        self._items[self._head] = None
        self._head += 1
        if self._head > 32 and self._head * 2 >= len(self._items):
            self._items = self._items[self._head:]
            self._head = 0
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[self._head]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self._items) - self._head

    def __len__(self):
        return self.size()

