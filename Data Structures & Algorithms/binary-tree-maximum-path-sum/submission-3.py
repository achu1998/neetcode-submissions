# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root):
        if root is None: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(self.ans, root.val, root.val+left, root.val+right, root.val+left+right)
        return root.val + max(left, right, 0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        self.dfs(root)
        return self.ans