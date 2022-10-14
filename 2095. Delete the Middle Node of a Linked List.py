# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        if len(temp) == 1:
            return 
        tmp =[]
        for i in range(len(temp)):
            if i == len(temp)//2:
                pass
            else:
                tmp.append(temp[i])
        
        head = ListNode(tmp[0])
        cur = head
        for i in range(1,len(tmp)):
            cur.next =ListNode(tmp[i])
            cur = cur.next
        return head
        print(tmp)