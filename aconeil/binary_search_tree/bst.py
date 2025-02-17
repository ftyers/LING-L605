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

    def inorder(self, level):
        if self.left:
            self.left.inorder(level+1)
        print(self, level)
        if self.right:
            self.right.inorder(level+1)

    def find(self, value, level):
        if value == self.value:
            #print(value, level)
            return level
        elif value < self.value:
            if self.left:
                return self.left.find(value, level+1)
        if self.right:
            return self.right.find(value, level+1)
        print("None")
    
    def delete(self, value, level):
        #if value == self.value:
            #print("Caution: Deleting the root")
            #del self.value
        #elif value < self.value:
            #print(self.value, self.left)
        if value != self.value:
            if self.left:
                return self.left.delete(value, level)
            elif self.right:
                return self.right.delete(value, level)
        elif self.left:
            print("has children")
        elif self.right:
            print("has children")
        else:
            print("Simple Delete")
            del self.value
            return

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
        level = 0
        if self.root:
            self.root.inorder(level)

    def find(self, value):
        level = 0
        if self.root:
            self.root.find(value, level)

    def delete(self, value):
        level = 0
        if self.root:
            level = self.root.find(value, level)
        if level != 'None':
            self.root.delete(value, level)

b= BinarySearchTree()
for value in [16, 7, 49, 4, 25, 64, 1, 9, 81, 52]:
    b.insert(value)

#b.inorder()
#b.find(16)
#b.find(12)
b.delete(1)
b.inorder()
