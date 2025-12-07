class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 2
        fast = 0
        if len(nums) < 2:
            return len(nums)
        for fast in range(2,len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow = slow + 1

        return slow 