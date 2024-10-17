#LeetCode: 2042. Check if Numbers Are Ascending in a Sentence
#Runtime: 29ms, Beats 87.53%
#Memory: 16.36MB, Beats 94.52%

#Given sentence, return true if all digits appear in ascending order

def areNumbersAscending(self, s: str) -> bool:
    lastnum = -1
    for token in s.split():
        if token.isdigit():
            if int(token) > lastnum:
                lastnum = int(token)
            else:
                return False
    
    return True
