#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. (Beat 60% of other submissions)
#Notice that the solution set must not contain duplicate triplets.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr = 0
        ans = []
        nums.sort()
        found = False
        for i1 in range(len(nums)):
            if i1 >0 and nums[i1] == nums[i1-1]:
                continue
            i2 = i1 + 1
            i3 = len(nums)-1
            while i2 < i3:
                curr = 0
                curr = nums[i1] + nums[i2] + nums[i3]
                if curr == 0:
                    item = [nums[i1],nums[i2],nums[i3]]
                    ans.append(item)                
                    while i2 < i3 and nums[i2] == nums[i2+1]:
                        i2 = i2 + 1
                    while i2 < i3 and nums[i3] == nums[i3-1]:
                        i3 = i3 -1
                    i2 = i2 + 1
                    i3 = i3 - 1
                elif curr < 0:
                    i2 = i2 + 1
                elif curr > 0:
                    i3 = i3-1
        return ans
