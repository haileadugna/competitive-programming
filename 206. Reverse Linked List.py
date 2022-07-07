# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=[]
        while head is not None:
            temp.append(head.val)
            head=head.next
        if temp==[]:
            return None
        else:
            head=ListNode(temp[-1])
            temp2=head
            for i in range(len(temp)-2, -1, -1):
                head.next=ListNode(temp[i])
                head=head.next
            return temp2  