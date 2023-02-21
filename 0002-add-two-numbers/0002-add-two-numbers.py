# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        temp = res
        rem = 0
        newNode1 = l1
        newNode2 = l2
        while newNode1 and newNode2:
            add = newNode1.val + newNode2.val  + rem
            res.next = ListNode(add % 10)
            rem = add//10
            res = res.next
            newNode1 = newNode1.next
            newNode2 = newNode2.next
        if newNode1 is None and newNode2 is None and rem != 0:
            res.next = ListNode(rem)
        
        if newNode1:
            while newNode1:
                add = newNode1.val + rem
                res.next = ListNode(add%10 )
                rem = add//10
                res = res.next
                newNode1 = newNode1.next
            if rem != 0:
                res.next = ListNode(rem)
        if newNode2:
            while newNode2:
                add = newNode2.val + rem
                res.next = ListNode(add%10 )
                rem = add//10
                res = res.next
                newNode2 = newNode2.next
            if rem != 0:
                res.next = ListNode(rem)
        return temp.next
            
         