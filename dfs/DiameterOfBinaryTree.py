def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    ans = [0]

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        
        # max ans can be right at this node, so we consider both paths
        ans[0] = max(ans[0], left + right + 1)

        # but we can continue down only 1 path
        return max(left, right) + 1

    dfs(root)
    return ans[0] - 1
