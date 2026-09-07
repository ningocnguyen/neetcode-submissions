# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy node for the scenario we have to delete the head or first node 
        # head=[1,2,3], n=3
        # so that left can do left.next = left.next.next 

        dummy=ListNode(0)
        dummy.next=head

        left=dummy
        right=dummy

        # move right n steps head
        for i in range(n):
            right=right.next

        while right.next: 
            right=right.next
            left=left.next

        left.next = left.next.next # skip the node after left

        return dummy.next