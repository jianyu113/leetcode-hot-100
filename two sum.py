class Solution(object):
    def twoSum(self, nums, target): 
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            target_num = target-nums[i]
            for j in range(i+1,len(nums)):
                if (nums[j]==target_num):
                    return [i,j]
        return []        
        """
        time complexity: O(n^2)
        space complexity: O(1)
        """
    
    def twoSum_optimized(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(0,len(nums)):
            target_num = target - nums[i]
            if target_num in num_dict:
                return [num_dict[target_num], i]
            num_dict[nums[i]] = i
        return []
        """
        time complexity: O(n)
        space complexity: O(n)
        """