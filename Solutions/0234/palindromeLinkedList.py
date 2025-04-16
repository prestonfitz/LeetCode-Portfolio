# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head.next if head else None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        current = slow.next
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # Step 3: Compare the first half and the reversed second half
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
        