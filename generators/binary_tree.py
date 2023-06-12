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
        if h == 1 and root:
            print(root.data, end=" ")
        elif root is not None:
            self.print_node_val(root.left, h-1)
            self.print_node_val(root.right, h-1)

    def level_order_recursive(self):
        h = self.height(self.root)
        for level in range(1, h+1):
            self.print_node_val(self.root, level)

    def preorder_iterative(self):
        s = list()
        s.append(self.root)
        temp = self.root
        while s:
            while temp:
                yield temp
                temp = temp.left
                if temp:
                    s.append(temp)
            if not s:
                break
            temp = s.pop()
            temp = temp.right
            if temp:
                s.append(temp)

    def lowest_common_ancestor(self, root, value_a, value_b):
        if root is None:
            return None
        if root.data == value_a or root.data == value_b:
            return root
        root_a = self.lowest_common_ancestor(root.left, value_a, value_b)
        root_b = self.lowest_common_ancestor(root.right, value_a, value_b)
        if root_a and root_b:
            return root
        return root_a if root_a else root_b


obj = BinaryTree()
for i in range(1, 16):
    obj.insert(i)

print("Print node data using bfs technique")
for node in obj.level_order():
    print(node.data, end=" ")

print("\nPrint node data using dfs technique")
obj.level_order_recursive()

print("\n Preorder traverse using iterative")
for node in obj.preorder_iterative():
    print(node.data, end=" ")

print("\nlca of 12 and 15")
print(obj.lowest_common_ancestor(obj.root, 12, 15).data)

print("lca of 5 and 7")
print(obj.lowest_common_ancestor(obj.root, 5, 7).data)

print("lca of 12 and 13")
print(obj.lowest_common_ancestor(obj.root, 12, 13).data)