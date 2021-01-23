# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        if len(heap) == 0:
            return None
        tup = heapq.heappop(heap)
        lists[tup[1]] = lists[tup[1]].next
        if lists[tup[1]]:
            heapq.heappush(heap, (lists[tup[1]].val, tup[1]))
        head = ListNode(tup[0])
        curr = head
        while len(heap) > 0:
            tup = heapq.heappop(heap)
            curr.next = ListNode(tup[0])
            lists[tup[1]] = lists[tup[1]].next
            curr = curr.next
            if lists[tup[1]]:
                heapq.heappush(heap, (lists[tup[1]].val, tup[1]))
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
    ll_lists = []
    for i in range(2):
        ll_lists.append(make_LL(range(i * 2)))
    leetsol = Solution()
    print_LL(leetsol.mergeKLists(ll_lists))
