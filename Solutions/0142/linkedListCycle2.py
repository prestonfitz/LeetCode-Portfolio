# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict = {}
        while head != None:
            if head in dict:
                return head
            else:
                dict[head] = True
            head = head.next
        return None
        