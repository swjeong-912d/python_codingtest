from collections import deque


# Goal : Armotized O(1) for all methods using queue
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.quer = deque()
        self.quel = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.quer:
            self.quel.append(x)
            while self.quer:
                self.quel.append(self.quer.popleft())
        else:
            self.quer.append(x)
            while self.quel:
                self.quer.append(self.quel.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.quer:
            return self.quer.popleft()
        else:
            return self.quel.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.quer:
            return self.quer[0]
        else:
            return self.quel[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.quer and not self.quel


def print_test():
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    print(obj.empty())
