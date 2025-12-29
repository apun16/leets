# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next: return
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        second, prev = slow.next, None
        slow.next = None
        while second:
            second.next, prev, second = prev, second, second.next
        
        p1, p2 = head, prev
        while p2:
            p1.next, p2.next, p1, p2 = p2, p1.next, p1.next, p2.next