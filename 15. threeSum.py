from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = set()
        
        for i in range(n-2):
            j = i+1
            k = n-1
            
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s==0: 
                    triplets.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif s<0: j+=1
                elif s>0: k-=1 
                    
        return triplets