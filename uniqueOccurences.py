#LeetCode: 1207. Unique Number of Occurrences
#Runtime: 35ms, Beats 89.81%
#Memory: 16.60MB, Beats 87.41%

def uniqueOccurrences(self, arr: List[int]) -> bool:
    occ = set()
    visited = set()
    for x in arr:
        if x not in visited:
            num = arr.count(x)
            if num in occ:
                return False
            else:
                occ.add(num)
                visited.add(x)
    return True
