# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            l1, l2 = l2, l1
        elif l2 is not None and l2.val < l1.val:
            l1, l2 = l2, l1
        lc = l1
        while lc is not None and l2 is not None:
            if lc.next is not None and lc.next.val > l2.val:
                lc.next, l2 = l2, lc.next
            elif lc.next is None and l2 is not None:
                lc.next = l2
                break
            lc = lc.next
        return l1


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
    print_LL(leet_sol.mergeTwoLists(make_LL([1]), make_LL([])))
