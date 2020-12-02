class Solution:
    def reverse(self, x: int) -> int:
        if x%10==x:
            return x
        elif x>0:
            x = int (str(x).rstrip('0')[::-1])
            return x if x <= ((1<<31)-1) else 0
        elif x<0:
            x = -int (str(abs(x)).rstrip('0')[::-1])
            return x if x >= -(1<<31) else 0