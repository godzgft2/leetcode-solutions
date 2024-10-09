#LeetCode: 921. Minimum Add to Make Parentheses Valid
#Runtime: 31ms, Beats 80.11%      O(n)
#Memory: 16.67 MB, Beats 31.13%   O(n)

#Returns minimum number of parentheses to add to make string valid

def minAddToMakeValid(self, s: str) -> int:
    stack = deque()
    count = 0
    
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                count += 1
    while stack:
        count += 1
        stack.pop()
    
    return count
