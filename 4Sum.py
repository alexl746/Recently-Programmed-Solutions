# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that: (Ran in 566 ms, beat 68% of submissions)
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        answer = []
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                p1 = b + 1
                p2 = len(nums) - 1
                while p1 < p2:
                    result = nums[a] + nums[b] + nums[p1] + nums[p2]
                    if result == target:
                        #answer.sort()
                        added = [nums[a],nums[b],nums[p1],nums[p2]]
                        #added.sort()
                        #add = True
                        #for i in range(len(answer)):
                        #    if added == answer[i]:
                        #        add = False
                        #if add == True:
                        while p1 < p2 and nums[p1] == nums[p1+1]:
                            p1 += 1
                        while p1 < p2 and nums[p2] == nums[p2-1]:
                            p2 -= 1
                        answer.append(added)
                        p1 += 1
                        p2 -= 1
                    elif result < target:
                        p1 += 1
                    elif result > target:
                        p2 -= 1
        return(answer)
