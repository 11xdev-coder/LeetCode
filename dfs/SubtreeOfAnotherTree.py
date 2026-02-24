# uses solution from 100. Is Same tree

def sameTree(self, p, q) -> bool:
    if not p and not q:
        return True
    
    if not p or not q:
        return False

    return p.val == q.val and self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return False

        # try to start same tree dfs
        if self.sameTree(node, subRoot):
            return True

        return dfs(node.left) or dfs(node.right)

    return dfs(root)