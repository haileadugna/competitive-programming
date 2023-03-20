# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        cur = dummy
        prev = None
        
        while cur.next:
            if cur.next.val == cur.val:
                prev.next = None
                temp = cur
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                else:
                    prev.next = temp.next
                cur = dummy

            else:
                prev = cur
                cur = cur.next

        return dummy.next
