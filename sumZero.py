#LeetCode: 1304. Find N Unique Integers Sum up to Zero
#Runtime 32ms, Beats 82.92%
#Memory 16.58MB, Beats 89.21%

#Creates array with length n that sums to zero

def sumZero(self, n: int) -> List[int]:
    ans = []
    if n % 2 != 0:
        ans.append(0)
    i = 1
    while len(ans) < n:
        ans.insert(0, -i)
        ans.append(i)
        i += 1
    return ans
