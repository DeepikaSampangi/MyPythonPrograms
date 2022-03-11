class Stack:
    def __init__(self):
        self.items: list = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        return len(self.items)


s: Stack = Stack()
print(s.isEmpty())

s.push(10)
s.push("Hello")
s.push("/")

print(s.peek())
print(s.size())
print(s)
print(s.items)
