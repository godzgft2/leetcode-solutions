// LeetCode: 74. Search a 2D Matrix
// Runtime 0 ms, Beats 100.00%
// Memory 12.02 MB, Beats 92.91%

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size(), n = matrix[0].size();
    int top = 0, bot = m-1;
    while (top <= bot) {    // Binary search for correct row
        int row = (bot + top)/2;
        if (target > matrix[row][n-1]) {
            top = row + 1;
        }
        else if (target < matrix[row][0]) {
            bot = row - 1;
        }
        else break;
    }

    if(top > bot) return false;   // If row with target not found
    
    int row = (bot + top)/2;
    int l = 0, r = n-1;
    while (l <= r) {      // Binary search for target in row
        int mid = (l+r)/2;
        if (target > matrix[row][mid]) {
            l = mid + 1;
        }
        else if (target < matrix[row][mid]) {
            r = mid - 1;
        }
        else {
            return true;
        }
    }
    return false;
}
