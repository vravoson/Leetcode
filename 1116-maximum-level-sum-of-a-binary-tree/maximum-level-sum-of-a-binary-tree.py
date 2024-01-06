# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dico_level = {}
        def bfs(root, depth):
            if root is None:
                return 0
            if depth not in dico_level:
                dico_level[depth] = root.val
            else:
                dico_level[depth] += root.val

            bfs(root.left, depth + 1)
            bfs(root.right, depth + 1)
        
        bfs(root, 1)
        max_sum = max(dico_level.values())
        for level,sum_val in dico_level.items():
            if sum_val == max_sum:
                return level
        