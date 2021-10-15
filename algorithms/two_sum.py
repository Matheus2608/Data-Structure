"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""


def twoSum(nums, target):
    complement_dic = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if nums[i] not in complement_dic:
            complement_dic[complement] = i
        else:
            return [complement_dic[nums[i]], i]
