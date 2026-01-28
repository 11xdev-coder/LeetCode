# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(node):
            if not node:
                return 0

            left_longest_path = dfs(node.left)
            right_longest_path = dfs(node.right)

            current_longest_path = 0
            left_gain = 0
            right_gain = 0
            if node.left and node.left.val == node.val:
                left_gain = left_longest_path + 1
            if node.right and node.right.val == node.val:
                right_gain = right_longest_path + 1

            current_longest_path = left_gain + right_gain

            ans[0] = max(ans[0], current_longest_path)
            # for parent -> only one branch
            return max(left_gain, right_gain)

        dfs(root)
        return ans[0]
