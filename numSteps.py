#LeetCode: 1404. Number of Steps to Reduce a Number in Binary Representation to One
#Runtime: 38ms, Beats 48.74%
#Memory: 16.48 MB, Beats 82.07%

def numSteps(self, s: str) -> int:
    num = 0
    steps = 0
    for i in range(len(s)):
        if int(s[i]) == 1:
            num += 2 ** (len(s) - 1 - i)
    while num != 1:
        if num % 2 == 0:
            num = num//2
        else:
            num += 1
        steps += 1

    return steps
