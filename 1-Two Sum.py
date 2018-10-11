'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
#by myself
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,k in enumerate(nums):
            for j,l in enumerate(nums):
                if i!=j:
                    if k+l == target:
                        return [i,j]

#others
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look_up = {}
        for i, num in enumerate(nums):
            if target-num in look_up:
                return [look_up[target-num], i]
            look_up[num] = i
        return []

