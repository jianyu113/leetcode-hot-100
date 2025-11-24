class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p1 = 0
        p2 = 0
        nums = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                nums.append(nums1[p1])
                p1 = p1 + 1
            else: 
                nums.append(nums2[p2])
                p2 = p2 + 1
        
        while p2 < len(nums2):
            nums.append(nums2[p2])
            p2 = p2 + 1

        while p1 < len(nums1):
            nums.append(nums1[p1])
            p1 = p1 + 1

        if len(nums) % 2 == 0:
            return float(nums[len(nums)/2] + nums[len(nums)/2-1])/2
        else:
            return float(nums[(len(nums)-1)/2])
