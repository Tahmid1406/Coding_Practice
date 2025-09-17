# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_valid_check(x: Optional[TreeNode], low:int, high: int) -> bool:

            #time
            O(n)
            #space
            O(1)
            
            if x is None:
                return True
            else:
                x_valid_flag = low < x.val < high
                left_valid_flag = dfs_valid_check(x.left, low, x.val)
                right_valid_flag = dfs_valid_check(x.right, x.val, high)
                valid_flag = x_valid_flag and left_valid_flag and right_valid_flag

                return valid_flag

        
        return dfs_valid_check(root, float('-inf'), float('inf'))
