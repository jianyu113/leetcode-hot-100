class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        substring = 0
        hashmap = {}

        for i in range(left, len(s)):

            char = s[i]
            if char in hashmap and hashmap[char]>=left:
                left = hashmap[char] + 1

            hashmap[char] = i
            substring = max(substring,i - left +1)
        
        return substring 