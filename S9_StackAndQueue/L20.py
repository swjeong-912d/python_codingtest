class ListNode:
    def __init__(self, val='', prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class Stack:
    def __init__(self):
        self.topn = None
    def push(self, ss: str):
        if self.empty():
            self.topn = ListNode(ss)
        else:
            prev = self.topn
            self.topn = ListNode(ss,prev,None)
            prev.next = self.topn
    def pop(self):
        if not self.empty():
            ss = self.topn.val
            self.topn = self.topn.prev
            if self.topn is not None:
                self.topn.next = None
    def top(self):
        if not self.empty():
            return self.topn.val
        else:
            return ""
    def empty(self):
        return self.topn is None


class Solution:
    def isValid(self, s: str) -> bool:
        str_stack = Stack()
        matchers = {'}':'{',')':'(',']':'['}
        for ss in s:
            if ss == '{' or ss == '(' or ss == '[':
                str_stack.push(ss)
            elif matchers[ss] != str_stack.top():
               return False
            else:
                str_stack.pop()
        return str_stack.empty()
def print_test():
    leet_sol = Solution()
    print(leet_sol.isValid("()"))