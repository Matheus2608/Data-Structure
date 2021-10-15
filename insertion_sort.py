"""
we keep the initial portion of the array sorted and insert the remaining elements one by one at the right position. It has time complexity of O(n**2) too.
"""


def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        print(nums)
        cur = nums.pop(i)
        j = i-1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums
