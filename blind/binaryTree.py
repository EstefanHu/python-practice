class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n, visited = len(maze), len(maze[0]), set()
        def dfs(x, y):
            if (x, y) not in visited:
                visited.add((x,y))
            else:
                return False

            if [x, y] == destination:
                return True

            for i, j in (0, -1), (0, 1), (-1, 0), (1, 0):
                new_X, new_Y = x, y
                while 0 <= new_X + i < m and 0 <= new_Y + j < n and maze[new_X + i][new_Y + j] != 1:
                    new_X += i
                    new_Y += j
                if dfs(new_X, new_y):
                    return True
            return False
        return (dfs(*start))

    def levelOrderRecursive(self, root):
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

    def levelOrderIterative(self, root):
        levels = []
        if not root: 
            return levels

        level = 0
        queue = deque([root,])
        while queue:
            levels.append([])
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
        return levels

    def zigZagBFS(self, root):
        res = []
        level_list = deque()
        if not root:
            return res

        node_queue = deque([root, None])
        zigging = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if :

        return res



