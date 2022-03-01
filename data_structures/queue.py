class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

    def peek(self):
        if not len(self.items) == 0:
            return self.items[-1]

    def next(self):
        if not len(self.items) == 0:
            return self.items[0]

    def get_all(self):
        return self.items

    def is_empty(self):
        if len(self.items) == 0:
            return True

a = Queue()
a.add(10)
a.add(20)
a.add(30)
a.add(40)
a.add(50)
print(a.get_all())
a.remove()
a.add(60)
print(a.get_all())
print(a.peek())
print(a.next())
