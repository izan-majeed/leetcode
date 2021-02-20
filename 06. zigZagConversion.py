class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        a = ["" for _ in range(numRows)]
        i, row = 0, 0
        while i<len(s):
            print(row, s[i])
            a[row] += s[i]
            row += 1
            i+=1
            if row==numRows :
                row -= 2
                while row>0 and i<len(s):
                    a[row] += s[i]
                    row -= 1
                    i+=1
        return ''.join(a)