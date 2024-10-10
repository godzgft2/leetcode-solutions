#LeetCode: 2696. Minimum String Length After Removing Substrings
#Runtime: 38ms, Beats 85.67%
#Memory: 16.62MB, Beats 14.96%

#Given string of all uppercase letters, return minimum possible
#length after removing substrings "AB" and "CD"

def minLength(self, s: str) -> int:
    stack = deque()
    removed = 0

    for ch in s:
        if ch == "A" or ch == "C":
            stack.append(ch)
        elif stack and ch == "B" and stack[-1] == "A":
            removed += 2
            stack.pop()
        elif stack and ch == "D" and stack[-1] == "C":
            removed += 2
            stack.pop()
        else:
            stack.clear()
    return len(s) - removed
