# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        next = head.next
        head.next = None
        while next is not None:
            nextnext = next.next
            next.next = head
            head = next
            next = nextnext
        return head
        # def reverseList_rec(head,next):
        #     if next is None:
        #         return head
        #     nextnext = next.next
        #     next.next = head
        #     head = next
        #     next = nextnext
        #     return reverseList_rec(head,next)
        # if head is None:
        #     return head
        # next = head.next
        # head.next = None
        # return reverseList_rec(head,next)

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
    print_LL(leet_sol.reverseList(make_LL([1,2,3,4,5,6])))
