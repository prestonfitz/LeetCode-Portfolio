# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and l1.next == None:
            return l2
        elif l2.val == 0 and l2.next == None:
            return l1

        word1 = ""
        word2 = ""
        temp = l1
        while temp:
            word1 = str(temp.val) + word1
            temp = temp.next

        temp = l2
        while temp:
            word2 = str(temp.val) + word2
            temp = temp.next

        # print(word1, word2)
        newNum = str(int(word1) + int(word2))
        
        lastNode = None
        for i in newNum:
            temp = ListNode(int(i), lastNode)
            lastNode = temp

        return temp
            