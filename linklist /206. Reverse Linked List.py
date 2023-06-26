class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        if not head:
            return pre
        
        while head:
            temp=ListNode(head.val)
            temp.next=pre
            pre=temp
            head=head.next
        return pre