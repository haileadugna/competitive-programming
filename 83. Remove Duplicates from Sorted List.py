# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = []
        
        while head is not None:
            dummy.append(head.val)
            head = head.next
        dumm = set(dummy)
        dummy = list(dumm)
        dummy.sort()
        if dummy == []:
            return None
        head = ListNode(dummy[0])
        temp = head
        for i in range(1, len(dummy)):
            head.next = ListNode(dummy[i])
            head = head.next
        return temp