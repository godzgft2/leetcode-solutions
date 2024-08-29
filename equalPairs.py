#LeetCode: 2352. Equal Row and Column Pairs
#Runtime: 399ms, Beats 56.26%
#Memory: 21.27MB, Beats 91.57%

#Given matrix, return number of pairs of rows and columns that are equal (same elements in the same order)

def equalPairs(self, grid: List[List[int]]) -> int:
    ans = 0
    unique_rows = dict()
    unique_cols = dict()

    for i in range(len(grid)):
        unique_rows[tuple(grid[i])] = unique_rows.get(tuple(grid[i]), 0) + 1
        col = []
        for j in range(len(grid)):
            col.append(grid[j][i])
        unique_cols[tuple(col)] = unique_cols.get(tuple(col), 0) + 1
    
    print(unique_rows, unique_cols)

    for line in unique_rows.keys():
        if line in unique_cols.keys():
            ans += unique_rows.get(line) * unique_cols.get(line)

    return ans
