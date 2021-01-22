class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front = 0
        self.dlen = 0
        self.vals = [0] * k
        self.vlen = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.vals[self.front] = value
        self.front -= 1
        if self.front < 0:
            self.front += self.vlen
        self.dlen += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.dlen += 1
        self.vals[(self.front + self.dlen) % self.vlen] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front += 1
        self.front %= self.vlen
        self.dlen -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.dlen -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.vals[(self.front + 1) % self.vlen]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.vals[(self.front + self.dlen) % self.vlen]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.dlen == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.dlen == self.vlen


# Your MyCircularDeque object will be instantiated and called as such:
def print_test():
    obj = MyCircularDeque(3)
    print(obj.insertLast(1))
    print(obj.insertLast(2))
    print(obj.insertFront(3))
