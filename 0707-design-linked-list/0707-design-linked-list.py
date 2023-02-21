class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        self.index = index
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            cur = cur.next
        if cnt <= self.index:
            return -1
        else:
            temp = self.head
            while self.index > 0 and temp:
                temp = temp.next
                self.index -= 1
            return temp.val
        

    def addAtHead(self, val: int) -> None:
        self.val = val
        newnode = ListNode(self.val)
        current = self.head
        newnode.next = current
        self.head = newnode
        # self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            cur = cur.next
        self.addAtIndex(cnt, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        self.index = index
        self.val = val
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            cur = cur.next

        if index > cnt:
            return

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        

    def deleteAtIndex(self, index: int) -> None:
        self.index = index
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            cur = cur.next
        if index < 0 or index >= cnt:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)




"""
            head=ListNode(temp[-1])
            temp2=head
            for i in range(len(temp)-2, -1, -1):
                head.next=ListNode(temp[i])
                head=head.next
            return temp2  

"""