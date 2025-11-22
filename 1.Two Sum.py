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
    
    # try to use hash map
    def twoSum_optimized(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(0,len(nums)):
            target_num = target - nums[i]
            if target_num in hash_map:
                return [hash_map[target_num],i]
            else:
                hash_map[nums[i]] =i

        return []