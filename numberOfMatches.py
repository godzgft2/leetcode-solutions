#LeetCode: 1688. Count of Matches in Tournament
#Runtime: 34 ms, Beats 63.3%
#Memory: 16.36 MB, Beats 93.84%

def numberOfMatches(self, n: int) -> int:
    matches = 0
    while n != 1:                  #Continue running until one team is left
        if n % 2 == 0:             #If even
            matches += n/2
            n = n/2
        else:                      #If odd
            matches += (n-1)/2
            n = (n-1)/2 +1
    return int(matches)
