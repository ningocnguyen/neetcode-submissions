# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # reverse 2nd list
        prev=None
        curr=slow.next
        slow.next=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        # combine 2 lists
        first=head
        second=prev

        while first and second:
            save1=first.next
            save2=second.next
            first.next=second
            first=save1
            second.next=save1
            second=save2