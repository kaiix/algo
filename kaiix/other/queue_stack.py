class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.rev_stk = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        stk = []
        while self.rev_stk:
            stk.append(self.rev_stk.pop())
        stk.append(x)
        while stk:
            self.rev_stk.append(stk.pop())

    # @return nothing
    def pop(self):
        self.rev_stk.pop()

    # @return an integer
    def peek(self):
        return self.rev_stk[-1]

    # @return an boolean
    def empty(self):
        return len(self.rev_stk) == 0


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    while not q.empty():
        print q.peek()
        q.pop()
