# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        ans = 0
        n = len(temp)
        for i in range(n):
            if temp[i] == 1:
                ans += 2**(n-i-1)
        return ans