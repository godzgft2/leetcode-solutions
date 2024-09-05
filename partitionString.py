#LeetCode: 2405. Optimal Partition of String
#Runtime: 90ms, Beats 57.69%
#Memory: 17.38MB, Beats 59.64%

def partitionString(self, s: str) -> int:
    unique = set()
    count = 1
    for char in s:
        if char in unique:
            count += 1
            unique.clear()
            unique.add(char)
        else:
            unique.add(char)
    return count
