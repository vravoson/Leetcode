# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def sum_rec(node, currentSum):
            if not node:
                return 0

            currentSum += node.val
            pathCount = 1 if currentSum == targetSum else 0
            
            pathCount += sum_rec(node.left, currentSum)
            pathCount += sum_rec(node.right, currentSum)

            return pathCount

        if not root:
            return 0

        return sum_rec(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        