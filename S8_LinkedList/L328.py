# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        tail_odd = head
        cur_even = head.next
        while cur_even and cur_even.next:
            cur_odd = cur_even.next
            next_even = cur_odd.next
            cur_odd.next = tail_odd.next
            tail_odd.next = cur_odd
            tail_odd = tail_odd.next
            cur_even.next = next_even
            cur_even = cur_even.next
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
    print_LL(leet_sol.oddEvenList(make_LL([1, 3, 5, 7, 9])))



