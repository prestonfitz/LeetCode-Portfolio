# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        while head and head.val == val:
            temp1 = head.next
            head.next = None
            head = temp1

        temp = head

        while temp:
            if temp.next:
                if temp.next.val == val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            else:
                temp = None

        return head
