# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        if root.left is None:
            return [root.val] + self.largestValues(root.right)
        if root.right is None:
            return [root.val] +  self.largestValues(root.left)
        else:
            left_list = self.largestValues(root.left)
            right_list = self.largestValues(root.right)
            l_length, r_length = len(left_list), len(right_list)
            if l_length <= r_length:
                res = [max(x,y) for x,y in zip(left_list, right_list[:l_length])]
                res += right_list[l_length:]
            else:
                res = [max(x,y) for x,y in zip(left_list[:r_length], right_list)]
                res += left_list[r_length:]

            return [root.val] + res
            
        