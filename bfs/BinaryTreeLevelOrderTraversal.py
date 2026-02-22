def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    queue = deque([root])

    order = []
    while queue:
        current_level_len = len(queue)
        current_level = []

        for _ in range(current_level_len):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        order.append(current_level)

    return order
