// Leetcode: 704. Binary Search
// Runtime 28ms, Beats 49.52%
// Memory 30.02MB, Beats 88.60%

int search(vector<int>& nums, int target) {
    int l = 0, r = nums.size()-1;
    while (l <= r) {
        int mid = l + (r-l)/2;
        if (nums[mid] > target) {
            r = mid - 1;
        }
        else if (nums[mid] < target) {
            l = mid + 1;
        }
        else {
            return mid;
        }
    }
    return -1;
}
