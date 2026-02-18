def maxDepth(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if not node:
            return 0

        # get max depth of children
        left = dfs(node.left)
        right = dfs(node.right)

        # we can only take 1 path and we maximize it
        return 1 + max(left, right)

    return dfs(root)
