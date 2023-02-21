# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
         
        slow = head
        stack = []
        stackind = []
        res = [0] * cnt
        ind = 0
        while slow:
            if not stack:
                stack.append(slow.val)
                stackind.append(ind)
                ind += 1

            elif stack and stack[-1] > slow.val:
                stackind.append(ind)
                stack.append(slow.val)
                ind += 1
                
            else:
                while stackind and stack and stack[-1] < slow.val:
                    res[stackind.pop()] = slow.val
                    stack.pop()
                   
                stack.append(slow.val)
                stackind.append(ind)
                ind += 1

            slow = slow.next
        return res 