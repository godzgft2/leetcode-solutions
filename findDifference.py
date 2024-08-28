#LeetCode: 2215. Find the Difference of Two Arrays
#Runtime: 144ms, Beats 46.43%
#Memory: 16.98MB, Beats 65.88%

def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    answer = [set(),set()]
    for i in range(max(len(nums1), len(nums2))):
        if i < len(nums1):
            if nums1[i] not in set2:
                answer[0].add(nums1[i])
        if i < len(nums2):
            if nums2[i] not in set1:
                answer[1].add(nums2[i])
    return answer
