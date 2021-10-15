"""
Merge_sort call itself invokes merge_sort twice (but with an array half the size), and also invokes the merge function once to merge the two resulting arrays. The two calls to merge_sort themselves make two recursive calls followed by an invocation of merge. The division continues till we reach an list of size 1 or 0. Thus, the merge sort algorithm ultimately boils down to a series of merge operations performed on arrays of varying sizes. Inside the merge function we perform comparisons and add numbers to a new array. So the time complexity of the merge function is n, where n is the lenght of the list before spliting.

The overall complexity of merge_sort is measured by how many times the merge function was invoked and the size of the input list for each invocation. In this case, the time complexity is O(nlog(n)).
"""


def merge(nums1, nums2):
    # List to store the results
    merged = []

    # Indices for iteration
    i, j = 0, 0

    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):

        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged array
    return merged + nums1_tail + nums2_tail


def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # Get the midpoint
    mid = len(nums) // 2

    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]

    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums
