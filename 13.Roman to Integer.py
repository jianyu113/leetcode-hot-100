class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        value = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        integer = 0

        for i in range(len(s)):
            if i+1 < len(s) and value[s[i]] < value[s[i+1]]:
                integer = integer -value[s[i]]
            else:
                integer = integer + value[s[i]]
                
        return integer
        