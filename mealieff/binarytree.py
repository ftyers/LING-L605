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

    def find(self, needle):
        if needle == self.value:
            return self

        if needle < self.value:
            if self.left:
                return self.left.find(needle)
        else:
            if self.right:
                return self.right.find(needle)

    def delete_node(self, value):
        # If the node is smaller or larger than the root, 
        if value < self.value:
            self.left = self.left.delete_node(self.left, value) 
        elif value > self.value:
            self.right = self.right.delete_node(self.right, value)
        # more complicated, need to find the node, then delete it, then rearrange?? 
        else:
            # the node has no children it can be deleted
            if self.left is None and self.right is None:
                return None
             # then go left and right 
            else:
                 # if the only child is on the right it can be promoted
                if self.left is None:
                    return self.right
                # ooh, actually left can be promoted too if it's the only child
                elif self.right is None:
                    return self.left
                else:
                    # both children are there, and their children??
                    # find the next lower node on the tree to the right of 'value'
                    get_min = self.right.inorder()
                    self.value = inorder_list[0] # Hmmm but leftmost elemet isn't naturally on the rightside of the root..
                    self.right = self.right.delete_node(self.value)
                    

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

#    def inorder(self, level):
#        if self.root:
#            self.root.inorder(level)
#            level += 1

    def inorder(self):
        if self.root:
            return self.root.inorder()
        return []

    def find(self, needle):
        if self.root:
            return self.root.find(needle)

    def delete_node(self, value):
        if self.root:
            self.root = self.delete_node(value)        

b = BinarySearchTree()
for value in [16, 1, 25, 7, 49, 64, 4, 9, 81, 52]:
    b.insert(value)


print("before deleting..", b.inorder())

b.delete_node(49)

print("before deleting..", b.inorder())
