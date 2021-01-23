class ListNode:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1021
        self.htable = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hkey = key % self.size
        if not self.htable[hkey]:
            self.htable[hkey] = ListNode(key, value)
        else:
            head = self.htable[hkey]
            while head.next:
                if head.key == key:
                    head.val = value
                    return
                head = head.next
            if head.key == key:
                head.val = value
                return
            else:
                head.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hkey = key % self.size
        if not self.htable[hkey]:
            return -1
        else:
            head = self.htable[hkey]
            while head:
                if head.key == key:
                    return head.val
                head = head.next
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hkey = key % self.size
        if self.htable[hkey]:
            head = self.htable[hkey]
            if head.key == key:
                self.htable[hkey] = head.next
                return
            while head.next:
                if head.next.key == key:
                    head.next = head.next.next
                    return
                head = head.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
