class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # use tuple for the set for searching same list faster
        nums.sort()             
        n = len(nums)
        res = set()             
        for i in range(n):
            target = -nums[i]
            seen = set()
            for j in range(i + 1, n):
                needed = target - nums[j]
                if needed in seen:
                    res.add((nums[i], needed, nums[j]))
                seen.add(nums[j])

        return [list(t) for t in res]
    
    