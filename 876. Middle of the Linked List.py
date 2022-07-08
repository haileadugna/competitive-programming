# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head is not None:
            temp.append(head.val)
            head = head.next
        n = len(temp)
        m = n//2
        nums = temp[m:]
        head = ListNode(nums[0])
        temp2 = head
        for i in range(1, len(nums)):
            head.next = ListNode(nums[i])
            head = head.next                      
        return temp2 