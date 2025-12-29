class Solution(object):
    def reorderList(self, head):
        listi = []
        curr = head
        
        while curr:
            listi.append(curr)
            curr = curr.next

        left = 0
        right = len(listi) - 1

        while left < right:
            listi[left].next = listi[right]
            left+=1
            listi[right].next = listi[left]
            right-=1
        listi[left].next = None
         
        return head