"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
"""

# Brute force solution


def count_rotations_linear(nums):
    position = 0                 # What is the intial value of position?

    # When should the loop be terminated?
    while position < len(nums):

        # Success criteria: check whether the number at the current position is smaller than the one before it
        # How to perform the check?
        if position > 0 and nums[position] < nums[position-1]:
            return position

        # Move to the next position
        position += 1

    return 0                     # What if none of the positions passed the check

# Optimal solution


def count_rotations_binary(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right) // 2
        mid_number = nums[mid]

        # Uncomment the next line for logging the values and fixing errors.
        print("left:", left, ", right:", right,
              ", mid:", mid, ", mid_number:", mid_number)

        if mid > 0 and mid_number < nums[mid-1]:
            # The middle position is the answer
            return mid

        elif nums[left] > mid_number:
            # Answer lies in the left half
            right = mid - 1

        else:
            # Answer lies in the right half
            left = mid + 1

    return 0
