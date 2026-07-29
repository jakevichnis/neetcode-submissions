# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen architecture keeping tracking of what has been seen by linked list by address so far
        addresses = set()
        # set current to head
        current = head
        # keep traversing list until None
        while current:
            if current in addresses:
                return True
            addresses.add(current)
            current = current.next
        # if we hit none there is no cycle, if we never do it will be implicit
        return False
