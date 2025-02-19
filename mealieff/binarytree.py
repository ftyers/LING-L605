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

    def get_min(self):
        if self.left is None:
            return self
        return self.left.get_min()

    def delete_node(self, value):
        if value < self.value:
            self.left = self.left.delete_node(value) 
        elif value > self.value:
            self.right = self.right.delete_node(value)
        else:
            if self.left is None and self.right is None:
                return None
            else:
                if self.left is None:
                    return self.right
                elif self.right is None:
                    return self.left
                else:
                    min_node = self.right.get_min()
                    self.value = min_node.value
                    self.right = self.right.delete_node(self.value)
        return self

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
            self.root = self.root.delete_node(value)        

    def pretty(self):
        root = self.root
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1  
        nlevels = height(root)
        width =  pow(2,nlevels+1)
    
        q=[(root,0,width,'c')]
        levels=[]
    
        while q:
            node, level, x, align = q.pop(0)
            if node:            
                if len(levels) <= level:
                    levels.append([])
            
                levels[level].append([node,level,x,align])
                seg= width // (pow(2, level+1))
                q.append((node.left, level+1, x - seg, 'l'))
                q.append((node.right, level+1, x + seg, 'r'))
    
        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i+1))
            for n in l:
                valstr = str(n[0].value)
                if n[3] == 'r':
                    linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    preline = n[2] 
                if n[3] == 'l':
                   linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)  
                   preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2] - pre - len(valstr)) + valstr #correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)   


b = BinarySearchTree()
for value in [16, 1, 25, 7, 49, 64, 4, 9, 81, 52]:
    b.insert(value)


print("before deleting..", b.inorder())

b.delete_node(49)

print("after deleting..", b.inorder())


b.delete_node(7)

print("after deleting..", b.inorder())

b.delete_node(81)

print("after deleting..", b.inorder())
