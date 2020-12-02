class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return 
        pair = {')': '(',
                '}': '{',
                ']': '[',
               }
        stack = []
        for i, x in enumerate(s):
            if x in ['(', '{', '[']:
                stack.append(x)
            else:
                if not stack or pair[x] != stack[-1]:
                    return False
                if pair[x] == stack[-1]:
                    stack.pop()
                
        if not stack:
            return True
        return False