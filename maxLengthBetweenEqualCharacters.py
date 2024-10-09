#LeetCode: 1624. Largest Substring Between Two Equal Characters
#Runtime 33ms, Beats 78.40%
#Memory 16.60 MB, Beats 28.86%

#Given string, find the maximum length between two equal characters

def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    unique = set()
    maxlen = -1
    for i in range(len(s)):
        if s[i] not in unique:
            unique.add(s[i])
        else:
            # (i - s.index(s[i]) - 1) is the current length between equal chars
            maxlen = max(maxlen, i - s.index(s[i]) - 1)
    
    return maxlen
