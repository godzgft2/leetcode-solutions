#LeetCode: 2044. Count Number of Maximum Bitwise-OR Subsets

#Counts the number of subsets of nums that have the maximum bitwise OR result

def countMaxOrSubsets(self, nums: List[int]) -> int:
    subset_list = []
    for i in range(len(nums)+1):
        subset_list.extend(combinations(nums, i))
    
    maxor = 0
    count = 0
    
    for subset in subset_list:
        OR = 0
        for num in subset:
            OR = OR | num
        if OR > maxor:
            count = 1
            maxor = OR
        elif OR == maxor:
            count += 1
        
    return count
