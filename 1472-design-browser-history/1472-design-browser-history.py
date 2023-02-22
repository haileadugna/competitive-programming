class ListNode:
    def __init__(self, val='', prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        new_node = ListNode(url, self.current)
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev:
                self.current = self.current.prev
            else:
                break
        return self.current.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next:
                self.current = self.current.next
            else:
                break
        return self.current.val