class MyQueue:
    
    def __init__(self):
        self.MyQueue = []
        self.MyQueue1 = []

    def push(self, x: int) -> None:
        while self.MyQueue:
            self.MyQueue1.append(self.MyQueue.pop())
        self.MyQueue.append(x)
        while self.MyQueue1:
            self.MyQueue.append(self.MyQueue1.pop())
    def pop(self) -> int:
        return self.MyQueue.pop()

    def peek(self) -> int:
        return self.MyQueue[-1]

    def empty(self) -> bool:
        if self.MyQueue == []:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()