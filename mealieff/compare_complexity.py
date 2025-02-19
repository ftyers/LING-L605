import time
import random
import matplotlib.pyplot as plt
import linkedlist
import binarytree

random.seed(42)

bt = binarytree.BinarySearchTree()
ll = linkedlist.LinkedList()

# Compare insertion and deletion : linked list and binary search tree

# 10000 - 100000
data = {}

for n in range(10000,100000):
    value = random.randint(10000, 100000)
    index = random.randint(10000, 100000)    

    start_time = time.time()
    ll.insert(index, value)
    ll_time = time.time() - start_time
    
    start_time = time.time()
    bt.insert(value)
    bst_time = time.time() - start_time

# Plot it
plt.figure(figsize=(10, 5))
plt.plot(n_values, ll_times, label='Linked List Insert Time', marker='o')
plt.plot(n_values, bst_times, label='BST Insert Time', marker='s')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Insertion Time Comparison: Linked List vs BST')
plt.legend()
plt.grid()
plt.show()
    
print(data)


 
