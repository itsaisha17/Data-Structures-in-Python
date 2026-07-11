# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        slow=head
        fast=head

        #gap=n
        count=0
        while count<n:          
            fast=fast.next
            count+=1
        #incase n=length of list
        if fast is None:
            return head.next
        #move both till fast reaches last , slow= Nth  then
        while fast.next:
            slow=slow.next
            fast=fast.next
        #delete Nth
        slow.next=slow.next.next
        return head
        