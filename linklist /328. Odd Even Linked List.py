class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even=ListNode(0,None)
        odd=ListNode(0,None)
        ans=odd
        anseven=even
        while head!=None:
            odd.next=ListNode(head.val,None)
            odd=odd.next
            if head.next!=None:
                even.next=ListNode(head.next.val,None)
                even=even.next
                head=head.next
            head=head.next
        odd.next=anseven.next
        return ans.next