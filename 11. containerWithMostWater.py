







# Brute force
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 minHeight = min(height[i], height[j])
#                 indexDiff = j-i
#                 count = max(count, minHeight*indexDiff)
#         return count 
