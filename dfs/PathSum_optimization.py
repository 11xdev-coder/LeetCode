# optimization -> we don't need to store all ways to get targetSum
# just return if we can find it

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    def dfs(node, remaining):
        # subtract remaining for this node
        remaining -= node.val

        # if this is a leaf, then we got correct sum
        if not node.left and not node.right and remaining == 0:
            return True

        # go further
        if node.left and dfs(node.left, remaining):
            return True # found path -> stop
        if node.right and dfs(node.right, remaining):
            return True

        # no path found
        return False

    return dfs(root, targetSum)