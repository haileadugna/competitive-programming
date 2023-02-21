# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        cur = head
        newNode = None
        while cur:
            prev = newNode
            newNode =  ListNode(cur.val)
            newNode.next = prev
            cur =  cur.next
        
        list1 = head
        list2 = newNode
        while list1 is not None and list2 is not None:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next

        if list1 is None and list2 is None:
            return True

        return False

        