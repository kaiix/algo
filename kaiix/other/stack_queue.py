from Queue import Queue


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = Queue()
        self.first = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if not self.first:
            self.first = x
        else:
            nq = Queue()
            nq.put(self.first)
            while not self.q.empty():
                nq.put(self.q.get())
            self.q = nq
            self.first = x

    # @return nothing
    def pop(self):
        if not self.q.empty():
            self.first = self.q.get()
        else:
            self.first = None

    # @return an integer
    def top(self):
        return self.first

    # @return an boolean
    def empty(self):
        return self.first is None


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.top()
    s.pop()
    print s.empty()
    print s.top()
    s.push(3)
    print s.empty()
    print s.top()
    s.pop()
    s.pop()
    s.pop()
    print s.empty()
