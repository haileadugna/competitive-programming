class StockSpanner:

    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span
        # ans = []
        # stack = []
        # for i in range(len(price)):
        #     while stack != [] and price[stack[-1]] <= price[i]:
        #         ind = stack.pop()
                
        #     stack.append(i)
        #     ans.append(i-ind + 1)
        #     ind = stack[-1]
        # print(stack)
        # print(ans)


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)