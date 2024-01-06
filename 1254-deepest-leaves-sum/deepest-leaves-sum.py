# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def max_depth(tree):
            if tree is None:
                return 0
            return 1+max(max_depth(tree.right), max_depth(tree.left))

        def deep_sum(root, depth, max_depth):
            if root is None:
                return 0
            elif depth == max_depth:
                return root.val
            return deep_sum(root.right, depth+1, max_depth)+deep_sum(root.left, depth+1, max_depth)
        
        max_depth = max_depth(root)
        return deep_sum(root, 1, max_depth)
            
