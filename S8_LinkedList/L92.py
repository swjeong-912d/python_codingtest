# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse_LL(head: ListNode):
            rtail = head
            rhead = head.next
            rtail.next = None
            prev_rhead = rtail
            while rhead:
                nhead = rhead.next
                rhead.next = prev_rhead
                prev_rhead = rhead
                rhead = nhead
            return prev_rhead, rtail
        subl = head
        left = head
        for i in range(1,m):
            left = subl
            subl = subl.next
        subr = subl
        for i in range(n-m):
            subr = subr.next
        right = subr.next
        subr.next = None
        subl, subr = reverse_LL(subl)
        if m > 1:
            left.next = subl
        else:
            head = subl
        subr.next = right
        return head



def make_LL(array):
    if len(array) == 0:
        return None
    head = ListNode()
    for (i, val) in enumerate(array):
        if i == 0:
            head.val = val
            curr = head
        else:
            ln = ListNode(val)
            curr.next = ln
            curr = curr.next
    return head

def print_LL(head):
    tail = head
    ll_list = []
    while tail is not None:
        ll_list.append(tail.val)
        tail = tail.next
    print(ll_list)

def print_test():
    leet_sol = Solution()
    print_LL(leet_sol.reverseBetween(make_LL([1, 2, 3, 4, 5]),1,1))



