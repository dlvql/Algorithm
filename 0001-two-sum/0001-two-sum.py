class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    break
        return ans