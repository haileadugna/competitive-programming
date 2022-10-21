# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        if  len(temp) == 0:
            return
        while k > 0:
            if k > len(temp):
                l, r  = 0, k
                while l <= r:
                    mid = (l + r)//2
                    if len(temp) * mid == k:
                        k -= len(temp) * mid
                    if len(temp)* mid > k:
                        r = mid -1
                    else:
                        l = mid + 1
                k -= len(temp) * r
            else:
                temp.insert(0, temp.pop())
                k -= 1
        head = ListNode(temp[0])
        cur = head
        for i in range(1, len(temp)):
            head.next = ListNode(temp[i])
            head = head.next
        return cur