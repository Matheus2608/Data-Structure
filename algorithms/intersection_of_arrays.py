def binary_search(a_list, target):
    left = 0
    right = len(a_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if a_list[mid] == target:
            return True
        elif a_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def intersect(nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    res = []
    if len(nums1) < len(nums2):
        for element in nums1:
            if binary_search(nums2, element):
                res.append(element)
    else:
        for element in nums2:
            if binary_search(nums1, element):
                res.append(element)
    return res
