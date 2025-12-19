# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return new_head

    """ 
    recursion

    optimal:
    prev = None 
        cur = head

        while cur:

            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev
    """
