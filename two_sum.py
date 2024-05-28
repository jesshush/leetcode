class Solution(object):
    def twoSum(self, nums, target):
        nums = [int(x) for i in input("Enter the numbers")]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
