def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    def dfs(node):
        if not node:
            return [0]

        if not node.left and not node.right:
            return [node.val]

        sums = []
        if node.left:
            left_sums = dfs(node.left)
            for s in left_sums:
                sums.append(s + node.val)

        if node.right:
            right_sums = dfs(node.right)
            for s in right_sums:
                sums.append(s + node.val)

        return sums

    return targetSum in dfs(root)
