class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        
        rows = [""]*numRows
        step = 0
        turn = 1
        for ch in s:
            rows[step] = rows[step] + ch
            if step == 0 :
                turn = 1
            elif step == numRows-1:
                turn = -1
            step = step + turn
        return "".join(rows)