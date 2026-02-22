def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    current_level = 0
    
    while queue:
        current_level += 1
        level_len = len(queue)

        for _ in range(level_len):
            node = queue.popleft()

            if not node.left and not node.right:
                return current_level

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

