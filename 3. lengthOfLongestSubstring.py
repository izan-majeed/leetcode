class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <=1: return len(s)
        result = set()
        i, j, max_ = 0, 0, 0
        while j < len(s):
            while s[j] in result:
                result.remove(s[i])
                i+=1
            result.add(s[j])
            max_ = max(max_, j-i+1)
            j+=1
        return max_