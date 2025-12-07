class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                nums[slow + 1] = nums[fast]
                slow = slow + 1

        return slow +1