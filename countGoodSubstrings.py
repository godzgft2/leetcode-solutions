#LeetCode: 1876. Substrings of Size Three with Distinct Characters
#Runtime 30ms, Beats 90.11%

#Counts number of substrings with length 3 with all different characters

def countGoodSubstrings(self, s: str) -> int:
    if len(s) < 3:
        return 0
    l, count = 0, 0
    while l != len(s)-2:
        print(s[l:l+3])
        if s[l] != s[l+1] and s[l] != s[l+2] and s[l+1] != s[l+2]:
            count += 1
        l += 1
        
    return count
