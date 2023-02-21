# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        
        n = cnt // 2
        stack = []
        temp = head
        while n > 0 :
            stack.append(temp.val)
            temp = temp.next
            n -= 1
            
        res = 0
        while temp :
            add = stack.pop() + temp.val
            temp = temp.next
            res = max(res, add)
        return res
        
        
        