class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # try to reverse half of the number to see whether it is equal to the orginal one
        if (x<0 or (x%10==0 and x!=0)):
            return False
        new_num = 0
        while (new_num<x):
            new_num = new_num * 10 + x%10
            x = x // 10
        return new_num == x or x == new_num // 10