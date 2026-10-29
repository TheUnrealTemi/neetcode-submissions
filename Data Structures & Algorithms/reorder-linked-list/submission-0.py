# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split the list by finding the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half of the list that starts from slow
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #head is the start of the first split, and prev is the start of the second
        prt1, prt2 = head, prev

        while prt2.next:
            temp1, temp2 = prt1.next, prt2.next
            prt1.next = prt2
            prt2.next = temp1
            prt1, prt2 = temp1, temp2
