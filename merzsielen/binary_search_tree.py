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
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def inorder(self):
        if self.root:
            self.root.inorder()
  
    def find(self, node, value):
        if (node.value == value): return node
        if (value < node.value and node.left):
            return self.find(node.left, value)
        if (value > node.value and node.right):
            return self.find(node.right, value)
        return None
    
    def delete(self, node, parent, value):
        #######################################################
        # Traversing the Tree                                 #
        #######################################################
        if (value < node.value and node.left != None):
            self.delete(node.left, node, value)
            return
        if (value > node.value and node.right != None):
            self.delete(node.right, node, value)
            return
        if (node.value != value):
            return

        #######################################################
        # Leaf Deletion                                       #
        #######################################################
        # We figure out whether this leaf is the left or
        # right branch of its parents and then clip it off.
        if (node.left == None and node.right == None):
            if (parent.left == node): parent.left = None
            else: parent.right = None
            return
        
        #######################################################
        # One-Child Node Deletion                             #
        #######################################################
        # We first figure out which of the branches is
        # empty and then promote the non-empty branch into
        # the position of the deleted node.
        if (node.left == None):
            if (parent.left == node): parent.left = node.right
            else: parent.right = node.right
            return
        elif (node.right == None):
            if (parent.left == node): parent.left = node.left
            else: parent.right = node.left
            return
        
        #######################################################
        # Two-Child Node Deletion                             #
        #######################################################
        # First, we find the leftmost node of the right
        # branch.
        target = node.right
        while (target != None and target.left != None):
            target = target.left

        # Then, we swap the original node's value for that
        # of the target.
        node.value = target.value

        # Finally, we recurse further down the tree and
        # delete the new target.
        self.delete(node.right, node, target.value)
        return

b = BinarySearchTree()
for value in [26, 93, 56, 63, 32, 25, 47, 34, 17, 8]:
    print('Inserting:',value)
    b.insert(value)

b.delete(b.root, None, 10)