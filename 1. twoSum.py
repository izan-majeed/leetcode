from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        complement = {}
        for i in range(n):
            c = target - nums[i]
            if c in complement.keys():
                return (complement[c], i)
            complement[nums[i]] = i

    def twoSumGeneral(self, nums: List[int], target: int) -> List[int]:
        complement = set()
        for i in range(len(nums)):
            if (target-nums[i]) in complement:
                return True
            complement.add(nums[i])
        return False