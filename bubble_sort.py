"""
There are two loops, each of length n-1, where n is the number of elements in nums. 
we can conclude that the time complexity of bubble sort is O(n**2).
"""


def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)

    # Repeat the process n-1 times
    for _ in range(len(nums) - 1):

        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):

            # 2. Compare the number with
            if nums[i] > nums[i+1]:

                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]

    # Return the sorted list
    return nums
