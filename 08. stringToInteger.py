class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s:
            x = ""
            sign = '+'

            if s[0] in '-+':
                sign = s[0]
                s = s[1:]

            for i in s:
                if i.isnumeric() or i == '.':
                    x += i
                else:
                    break
            try:
                x = -int(float(x)) if sign=='-' else int(float(x))
                if -2**31 <= x <= (2**31)-1:
                    return x
                elif x < -2**31:
                    return -2**31
                elif x > (2**31)-1:
                    return (2**31)-1
            except ValueError:
                return 0
        return 0