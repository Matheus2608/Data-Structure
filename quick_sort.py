"""
1.If the list is empty or has just one element, return it. It's already sorted.
2.Pick a random element from the list. This element is called a pivot.
3.Reorder the list so that all elements with values less than or equal to the pivot come before the pivot, while all elements with values greater than the pivot come after it. This operation is called partitioning.
4.The pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort.
"""

"""
If we partition the list into two nearly equal parts, then the complexity analysis is similar to that of merge sort and quicksort has the complexity O(nlog(n))
In this case, the partition is called n times with lists of sizes n, n-1... so that total comparisions are n + (n - 1) + (n - 2)... + 1 = n*(n-1)/2. So the time complexity would be O(n**2).
"""


def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end-1

    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums
