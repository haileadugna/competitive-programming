class MinStack:

    def __init__(self):
        self.stack = []
        self.getmin = []
    def push(self, val: int) -> None:
        if len(self.stack) != 0:
            if self.getmin[-1] >= val:
                self.getmin.append(val)
        else:
            self.getmin.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        temp = self.stack.pop()
        if len(self.stack) != 0:
            if self.getmin[-1] == temp:
                self.getmin.pop()
            return temp

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.getmin) != 0 :
            return self.getmin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()