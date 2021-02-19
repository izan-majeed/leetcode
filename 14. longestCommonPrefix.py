from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        if len(strs)==1: return strs[0]
        strs.sort()
        lcp = ''
        #e.g [lee, ... leetcode] --> [(l, l), (e, e), (e, e)]
        for x, y in zip(strs[0], strs[-1]):
            if x == y: lcp += x
            else: break
        return lcp
