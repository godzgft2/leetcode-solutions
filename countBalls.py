#LeetCode: 1742. Maximum Number of Balls in a Box
#Runtime: 376ms, Beats 53.77%
#Memory: 16.48MB, Beats 78.25%

#Places balls numbered from lowLimit to highLimit in boxes based on 
#sum of its digits, then return the highest number of balls in a box

def countBalls(self, lowLimit: int, highLimit: int) -> int:
    freq = defaultdict(int)

    for num in range(lowLimit, highLimit + 1):
        sumdigits = 0
        for digit in str(num):
            sumdigits += int(digit)
        freq[sumdigits] += 1
    
    return max(freq.values())
