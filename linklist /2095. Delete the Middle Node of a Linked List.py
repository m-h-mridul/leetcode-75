# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2=head
        count=0
        while head:
            head=head.next
            count+=1
        
        count=count//2
        head3=head2
        temp=0
        while head2:
            if temp==count-1:
                if head2.next.next:
                    head2.next=head2.next.next
                else:
                    head2.next=None
                break
            head2=head2.next
            temp+=1
        if count==0:
            head3=None
        return head3 
            