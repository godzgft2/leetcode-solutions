#LeetCode: 872. Leaf-Similar Trees
#Runtime: 41ms, Beats 19.71%
#Memory: 16.49MB, Beats 88.73%


def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

    def DFS(root, seq):
        if root == None:
            return
        if root.left == None and root.right == None:
            seq.append(root.val)
        DFS(root.left, seq)
        DFS(root.right, seq)

    seq1 = []
    DFS(root1, seq1)

    seq2 = []
    DFS(root2, seq2)


    if seq1 == seq2:
        return True
    else:
        return False
