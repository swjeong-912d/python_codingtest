from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        th = (len(nums) + 1) // 2
        for num in nums:
            dic[num] += 1
            if dic[num] >= th:
                return num
