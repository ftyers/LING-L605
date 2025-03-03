import time
import random
import matplotlib.pyplot as plt
import linkedlist
import binarytree
import numpy as np
import heap

random.seed(42)

bt = binarytree.BinarySearchTree()
ll = linkedlist.LinkedList()
hp = heap.Heap()

# Compare insertion and deletion : linked list and binary search tree

# 10000 - 100000

n_values = list(range(10000, 100000, 5000))
ll_times_avg = []
bst_times_avg = []
hp_times_avg = []
num_trials = 100 


for n in n_values:
    ll_times = []
    bst_times = []
    hp_times = []
    for i in range(num_trials):
        value = random.randint(10000, 100000)
    
        start_time = time.time()
        ll.append(value) # issues with insert, no
        ll_times.append(time.time() - start_time)

        start_time = time.time()
        bt.insert(value)
        bst_times.append(time.time() - start_time)

        start_time = time.time()
        hp.insert(value)
        hp_times.append(time.time() - start_time)

    ll_times_avg.append(sum(ll_times) / num_trials)
    bst_times_avg.append(sum(bst_times) / num_trials)
    hp_times_avg.append(sum(hp_times) / num_trials)
print(len(n_values))
print(len(ll_times_avg))
print(len(bst_times_avg))

# Include a line of best fit

ll_fit = np.polyfit(n_values, ll_times_avg, 1)
bst_fit = np.polyfit(n_values, bst_times_avg, 1)
hp_fit = np.polyfit(n_values, hp_times_avg, 1)

ll_fit_line = np.poly1d(ll_fit)
bst_fit_line = np.poly1d(bst_fit)
hp_fit_line = np.poly1d(hp_fit)


# Plot results
plt.figure(figsize=(10, 5))
plt.plot(n_values, ll_times_avg, label='Linked List Time', marker='o')
plt.plot(n_values, bst_times_avg, label='BST Time', marker='s')
plt.plot(n_values, hp_times_avg, label='Heap Insert', marker='^')

plt.plot(n_values, ll_fit_line(n_values), label='LL Best Fit', linestyle='--')
plt.plot(n_values, bst_fit_line(n_values), label='BST Best Fit', linestyle='--')
plt.plot(n_values, hp_fit_line(n_values), label='Heap Best Fit', linestyle='--')

plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Insertion Time Comparison: Linked List vs BST vs Heap')
plt.legend()
plt.grid()
plt.show()
    
#print(data)


 
