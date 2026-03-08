def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False
        
        # left node must be more than lowest but < node
        # right node must be less than highest but > node
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
    return dfs(root, float('-inf'), float('inf'))
