class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""

        for i in range(0,len(strs[0])):
            ch = strs[0][i]
            flag = True

            for s in strs:
                if i >= len(s) or s[i] != ch:
                    return prefix

            if flag == True:
                prefix = prefix + ch

        return prefix