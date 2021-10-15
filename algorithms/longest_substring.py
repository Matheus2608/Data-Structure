def lengthOfLongestSubstring(s: str) -> int:
    chars = [0] * 128
    left, res = 0, 0
    for right in range(len(s)):
        while chars[ord(s[right])] > 0:
            chars[ord(s[left])] -= 1
            left += 1
        chars[ord(s[right])] = 1
        res = max(res, right - left + 1)
    return res


print(lengthOfLongestSubstring("abcabcbb"))
