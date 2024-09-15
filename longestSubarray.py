#LeetCode: 2419. Longest Subarray With Maximum Bitwise AND
#Runtime: 630ms, Beats 79.58%
#Memory: 31.02MB, Beats 65.85%

import sys
def longestSubarray(self, nums: List[int]) -> int:
    maxsum = maxlen = 0
    temp = sys.maxsize
    templen = 0
    for num in nums:
        temp = temp & num
        if num > maxsum:
            temp = num
            maxsum = num
            maxlen = 1
            templen = 1
        elif temp >= maxsum:
            maxsum = temp
            templen += 1
            if templen > maxlen:
                maxlen = templen
        else:
            templen = 0
            temp = sys.maxsize
    return maxlen
