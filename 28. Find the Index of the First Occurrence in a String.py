class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
    
        for i in range(0, len(haystack)-len(needle) + 1):

            if haystack[i] == needle[0]:

                if len(needle) == 1:
                    return i

                k = i + 1
                for j in range(1,len(needle)):
                    if haystack[k] != needle[j]:
                        break
                    if j == (len(needle)-1) and  haystack[k] == needle[j]:
                        return i
                    k = k + 1

        return -1
                    