# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def merge(l_tail, l):
            prev = l_tail
            l_tail = ListNode()
            l_tail.val = l.val
            if prev != None:
                prev.next = l_tail
            return l_tail

        if l1 is None and l2 is None:
            return None
        head = ListNode()
        is_l1_head = True
        if l1 is None or (l2 and l1 is not None and l1.val >= l2.val):
            is_l1_head = False
        if is_l1_head:
            head.val = l1.val
            l1 = l1.next
        else:
            head.val = l2.val
            l2 = l2.next
        tail = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tail = merge(tail, l1)
                l1 = l1.next
            else:
                tail = merge(tail, l2)
                l2 = l2.next

        while l1 is not None:
            tail = merge(tail, l1)
            l1 = l1.next
            if head == None:
                head = tail
        while l2 is not None:
            tail = merge(tail, l2)
            l2 = l2.next
            if head == None:
                head = tail
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
    print_LL(leet_sol.mergeTwoLists(make_LL([1, 2, 4]), make_LL([1, 3, 4])))
