#LeetCode: 1492. The kth Factor of n
#Runtime 40ms, Beats 26.41%    O(n) (specifically n/2)
#Memory 16.54MB, Beats 56.42%  O(1)

#Given a number find its kth factor in ascending order

def kthFactor(self, n: int, k: int) -> int:
    count = 0
    #Loops from 1 to n/2, no more factors after n/2 other than n
    for num in range(1, (n//2)+1):
        if n % num == 0:
            count += 1
            if count == k:
                return num
    #If next factor is kth, it is n
    if count+1 == k:
        return n
    return -1
