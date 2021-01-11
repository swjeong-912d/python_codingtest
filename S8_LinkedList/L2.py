# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        h1 = l1
        h2 = l2
        while h1 is not None and h2 is not None:
            h1 = h1.next
            h2 = h2.next
        if h1 is None:
            h1, h2 = l2, l1
        else:
            h1, h2 = l1, l2

        head = h1
        while h1 is not None and h2 is not None:
            h1.val += h2.val
            if h1.val >= 10:
                if h1.next is not None:
                    h1.next.val += int(h1.val/10)
                else:
                    h1.next = ListNode(int(h1.val/10))
                h1.val %= 10
            h1 = h1.next
            h2 = h2.next
        while h1 is not None:
            if h1.val >= 10:
                if h1.next is not None:
                    h1.next.val += int(h1.val/10)
                else:
                    h1.next = ListNode(int(h1.val/10))
                h1.val %= 10
            h1 = h1.next
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
    print_LL(leet_sol.addTwoNumbers(make_LL([9,9,9,9]), make_LL([9,9,9,9,9,9,9])))
