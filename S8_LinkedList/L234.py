# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        rev = head
        fast = head
        while fast is not None:
            if fast.next is not None:
                fast = fast.next.next
                rev = rev.next
            else:
                break

        revp = None
        rev = rev
        revn = rev.next
        while rev is not None:
            rev.next = revp
            revp = rev
            rev = revn
            if revn is not None:
                revn = revn.next

        itr1 = head
        itr2 = revp
        while itr1 is not None and itr2 is not None:
            if itr1.val == itr2.val:
                itr1 = itr1.next
                itr2 = itr2.next
            else:
                return False
        return True
def make_LL(array):
    if len(array) == 0:
        return None
    head = ListNode()
    for (i,val) in enumerate(array):
        if i == 0:
            head.val = val
            curr = head
        else:
            ln = ListNode(val)
            curr.next = ln
            curr = curr.next
    return head

def print_test():
    leet_sol = Solution()
    print(leet_sol.isPalindrome(make_LL([1,2,2])))







