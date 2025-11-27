class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1
        new_num = 0

        if x < 0:
            sign = -1
            x = abs(x)
        
        while x != 0:
            new_num = new_num*10 + x % 10
            x = x // 10
        
        result = new_num * sign

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
        