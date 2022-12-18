# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        while l1 is not None:
            str1 = str(l1.val) + str1
            l1 = l1.next
        while l2 != None :
            str2 = str(l2.val) + str2
            l2 = l2.next
        summ = eval(str1+"+"+str2)
        summ = str(summ)
        head = ListNode(int(summ[-1]))
        temp = head
        for i in summ[-2::-1]:
            head.next = ListNode(int(i))
            head = head.next
        return temp
        