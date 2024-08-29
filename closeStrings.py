#LeetCode: 1657. Determine if Two Strings Are Close
#Runtime: 189ms, Beats 50.17%
#Memory: 17.85MB, Beats 41.55%

def closeStrings(self, word1: str, word2: str) -> bool:

    counts1 = dict()
    for char in word1:
        counts1[char] = counts1.get(char, 0) + 1
    
    counts2 = dict()
    for char in word2:
        counts2[char] = counts2.get(char, 0) + 1

    if len(counts1) != len(counts2) or set(counts1.keys()) != set(counts2.keys()):
        return False

    l1 = list(counts1.values()) 
    l2 = list(counts2.values())

    l1.sort()
    l2.sort()

    if l1 != l2:
        return False
    
    return True
