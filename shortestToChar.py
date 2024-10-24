#LeetCode: 821. Shortest Distance to a Character
#Runtime: 35ms, Beats 85.30%
#Memory: 16.70MB, Beats 55.56%

# Given string and specific character, return array of all indices' minimum distances to character

def shortestToChar(self, s: str, c: str) -> List[int]:
    charPos = []
    for i in range(len(s)):
        if s[i] == c:
            charPos.append(i)
    ans = [0] * len(s)
    for i in range(len(ans)):
        minDist = len(s)
        for pos in charPos:
            minDist = min(minDist, abs(pos-i))
        ans[i] = minDist
    return ans
