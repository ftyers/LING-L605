class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def find(self, value):
        # print(value)
        if self.value == value:
            print(value,'is here.')
            return
        if value < self.value and self.left:
            self.left.find(value)
        elif value > self.value and self.right:
            self.right.find(value)
        else:
            print(value,'is not here.')

    def delete(self, value):
        if value < self.value and self.left:
            self.left = self.left.delete(value)
        elif value > self.value and self.right:
            self.right = self.right.delete(value)
        elif self.value == value:
            # print(f"{value} is here.")

            # no branches
            if not self.left and not self.right:
                return None

            # one branch
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            # two branches, find the smallest value in the right
            replacement = self.right
            while replacement.left:
                replacement = replacement.left

            # replace to-be-deleted node's value with replacement's value
            self.value = replacement.value

            # delete replacement node from the right
            self.right = self.right.delete(replacement.value)

        return self

    def __str__(self):
        return '['+str(self.value)+']'

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def pretty(self):
        root = self.root

        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        nlevels = height(root)
        width = pow(2, nlevels + 1)

        q = [(root, 0, width, 'c')]
        levels = []

        while q:
            node, level, x, align = q.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level + 1))
                q.append((node.left, level + 1, x - seg, 'l'))
                q.append((node.right, level + 1, x + seg, 'r'))

        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i + 1))
            for n in l:
                valstr = str(n[0].value)
                if n[3] == 'r':
                    linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    preline = n[2]
                if n[3] == 'l':
                    linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                    preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def find(self, value):
        if self.root:
            self.root.find(value)
        else:
            print('Tree is empty.')

    def inorder(self, node=None, a=""):
        if node:
            self.inorder(node.left, a + '\t')
            print(a + str(node.value))
            self.inorder(node.right, a + '\t')

    # def inorder_traversal(self, root, result):
    #     if root:
    #         self.inorder_traversal(root.left, result)
    #         result.append(str(root.value))
    #         self.inorder_traversal(root.right, result)

    # def __str__(self):
    #     result = []
    #     self.inorder_traversal(self.root, result)
    #     return " -> ".join(result)  # Format as an arrow-separated string



    def delete(self, value):
        """Public delete function."""
        if self.root:
            self.root = self.root.delete(value)
        else:
            print("Tree is empty.")


b = BinarySearchTree()
for value in [16, 7, 49, 4, 24, 65, 1, 9, 81, 52]:
        b.insert(value)

print(b)

b.find(16)
b.find(7)
b.find(3)

print(b)
a = ''
b.inorder(b.root, a)

b.delete(49)

print(b)
a = ''
b.inorder(b.root, a)

b.delete(7)

print(b)
a = ''
b.inorder(b.root, a)
