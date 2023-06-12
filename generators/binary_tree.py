class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        q = list()
        q.append(self.root)
        while True:
            temp = q.pop(0)
            if temp.left is None:
                temp.left = Node(data)
                break
            if temp.right is None:
                temp.right = Node(data)
                break
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

    def level_order(self):
        q = list()
        q.append(self.root)
        while q:
            temp = q.pop(0)
            yield temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

    def height(self, root):
        if root is None:
            return 0
        return 1+max(self.height(root.left), self.height(root.right))

    def print_node_val(self, root, h):
        if h < 1:
            return
        if h == 1:
            print(root.data, end=" ")
        else:
            self.print_node_val(root.left, h-1)
            self.print_node_val(root.right, h-1)
    def level_order_dfs(self):
        h = self.height(self.root)
        for level in range(1, h+1):
            self.print_node_val(self.root, level)


obj = BinaryTree()
for i in range(1, 16):
    obj.insert(i)

for node in obj.level_order():
    print(node.data)

obj.level_order()
