# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lst = []
        p = head
        while p:
            lst.append(p.val)
            p = p.next
        lst.sort()
        p = head
        i = 0
        while p:
            p.val = lst[i]
            i += 1
            p = p.next
        return head
