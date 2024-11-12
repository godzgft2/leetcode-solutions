# LeetCode: 2070. Most Beautiful Item for Each Query
# Runtime: O(M * logM + N * logN)    M - size of items
# Memory: O(M + N)                   N - size of queries

# Given items where item[i] = [price, beauty] and query is a list of prices,
# return the maximum beauty for each query, where item price <= query price

def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    ans = [0] * len(queries)
    items.sort(key=lambda x: x[0])
  
    query_indices = [[queries[i], i] for i in range(len(queries))] 
    query_indices.sort(key=lambda x: x[0])
  
    beauty = 0
    itempos = 0
  
    for i in range(len(queries)):
        query = query_indices[i][0]
        og_index = query_indices[i][1]

        while itempos < len(items) and items[itempos][0] <= query:
            beauty = max(beauty, items[itempos][1])
            itempos += 1
        
        ans[og_index] = beauty
    
    return ans
