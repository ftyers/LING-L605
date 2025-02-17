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

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self)
        if self.right:
            self.right.inorder()
                
    def __str__(self):
        return '['+str(self.value)+']'

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root: # If we have already defined the root
                # call the insert function of the root node
            self.root.insert(value)
        else:    # define the root
            self.root = Node(value)

    def inorder(self):
        if self.root:
            self.root.inorder()

    # def find(self, value):
    #     node = self.root
    #     while(True):
    #         if (node.value == value): return node
    #         if (value < node.value and node.left):
    #             node = node.left
    #             continue
    #         if (value > node.value and node.right):
    #             node = node.right
    #             continue
    #         return None
            
    def find(self, node, value):
        if (node.value == value): return node
        if (value < node.value and node.left):
            return self.find(node.left, value)
        if (value > node.value and node.right):
            return self.find(node.right, value)
        return None
    
    def delete(self, node, parent, value):
        if (value < node.value and node.left != None):
            self.delete(node.left, node, value)
            return
        if (value > node.value and node.right != None):
            self.delete(node.right, node, value)
            return
        if (node.value != value):
            return

        # If the node has no children, just prune it entirely.
        if (node.left == None and node.right == None):
            if (parent.left == node): parent.left = None
            else: parent.right = None
            return
        
        # If the node has only one child, just replace the
        # corresponding parent branch with that.
        if (node.left == None):
            if (parent.left == node): parent.left = node.right
            else: parent.right = node.right
            return
        elif (node.right == None):
            if (parent.left == node): parent.left = node.left
            else: parent.right = node.left
            return
        
        # If the node has more than one child, we find the
        # next node in-order, replace the current node with
        # that one, and then delete.
        target = node.right
        while (target != None and target.left != None):
            target = target.left
        node.value = value
        self.delete(node.right, node, value)
        return

b = BinarySearchTree()
for value in [16, 7, 49, 4, 25, 64, 1, 9, 10, 81, 52]:
    print('Inserting:',value)
    b.insert(value)

b.delete(b.root, None, 10)