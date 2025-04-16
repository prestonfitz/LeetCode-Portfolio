# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        setList = set()

        while head:
            print(setList)
            setList.add(head.val)
            head = head.next
        
        listList = list(setList)
        listList.sort(reverse=True)

        nextNode = None
        for i in listList:
            head = ListNode(i, nextNode)
            nextNode = head

        return head