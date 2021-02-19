from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = merge(nums1, nums2)
        mid = len(a)//2
        if len(a)%2==0:
            return (a[mid]+a[mid-1])/2
        else:
            return a[mid]
def merge(nums1, nums2):
    if len(nums1)==0:
        return nums2
    if len(nums2)==0:
        return nums1
    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    k = 0
    a = [None]*(n+m)

    while i<n and j<m:
        if nums1[i] <= nums2[j]:
            a[k] = nums1[i]
            i+=1
            k+=1
        elif nums2[j] <= nums1[i] :
            a[k] = nums2[j]
            j+=1
            k+=1
    while (i<n):
        a[k] = nums1[i]
        i+=1
        k+=1
    while (j<m):
        a[k] = nums2[j]
        j+=1
        k+=1
    return a