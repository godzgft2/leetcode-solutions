#LeetCode: 392. Is Subsequence
#Runtime: 33ms, Beats 75.01%
#Memory: 16.62MB, Beats 20.04%

#Return True if string s can be created by removing any number of elements from string t, while keeping order

def isSubsequence(self, s: str, t: str) -> bool:
    if s == "":                      #if s is empty string always true
        return True
    if len(s) > len(t):              #if s is longer than t never true
        return False
    if len(s) == len(t):             #if equal length, only true when strings are the same
        if s == t:
            return True
        else:
            return False
    idx = 0
    for i in range(len(t)):          #Loop to check each char in s against t
        if s[idx] == t[i]:
            idx = idx + 1
            if idx == len(s):        #If index of s incremented to the end, return True
                return True
    return False
