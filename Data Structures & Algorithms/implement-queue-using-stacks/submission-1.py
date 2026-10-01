class MyQueue:

    def __init__(self):
        self.queue = []
        self.aux = []
        self.fst=0
        self.l = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.l += 1
        

    def pop(self) -> int:
        if self.empty():
            return None
        c = self.l
        while c > 1:
            e = self.queue.pop()
            self.aux.append(e)
            c -= 1
        res = self.queue.pop()
        while self.aux:
            e = self.aux.pop()
            self.queue.append(e)
        self.l -= 1
        return res 
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return not bool(self.l)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()