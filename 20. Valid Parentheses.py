class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        add = []
        left_right = {'(':')','{':'}','[':']'}
        for br in s:
            if br in left_right.keys():
                add.append(br)
            else:
                if len(add) == 0:
                    return False
                if br == left_right[add[-1]]:
                    top = add.pop() 
                else:
                    return False
        return len(add) == 0