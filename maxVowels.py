#LeetCode: 1456. Maximum Number of Vowels in a Substring of Given Length
#Runtime: 129ms, Beats 47.72%
#Memory: 17.33MB, Beats 55.44%

def maxVowels(self, s: str, k: int) -> int:
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    left = 0
    right = k-1
    temp = s[:right+1]

    for char in temp:
        if char in vowels:
            count += 1
    
    maxc = count              #Initialize max number as number in first substring

    while right < len(s):     #Loop increments sliding window, subtracting and adding vowels from count
        left += 1
        right += 1
        if s[left-1] in vowels:
            count -= 1
        if right < len(s) and s[right] in vowels:
            count += 1
        if count > maxc:
            maxc = count


    return maxc
