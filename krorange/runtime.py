import time
import random
import matplotlib.pyplot as plt
import numpy as np

import linkedlist
import binarytree

random.seed(42)

bt = binarytree.BinarySearchTree()
ll = linkedlist.LinkedList()

n_values = list(range(10000, 100001, 5000))

ll_insert_times_avg = []
bt_insert_times_avg = []

num_trials = 10

for n in n_values:
    ll_insert_times = []
    bt_insert_times = []

    for _ in range(num_trials):
        values = [random.randint(0, 1000000) for _ in range(n)]

        start_time = time.time()
        for value in values:
            ll.append(value)
        ll_insert_times.append(time.time() - start_time)

        start_time = time.time()
        for value in values:
            bt.insert(value)
        bt_insert_times.append(time.time() - start_time)

    ll_insert_times_avg.append(sum(ll_insert_times) / num_trials)
    bt_insert_times_avg.append(sum(bt_insert_times) / num_trials)

ll_insert_fit = np.poly1d(np.polyfit(n_values, ll_insert_times_avg, 1))
bt_insert_fit = np.poly1d(np.polyfit(n_values, bt_insert_times_avg, 1))

plt.figure(figsize=(10, 5))
plt.plot(n_values, ll_insert_times_avg, label="Linked List Insert", marker='o')
plt.plot(n_values, bt_insert_times_avg, label="BST Insert", marker='s')
plt.plot(n_values, ll_insert_fit(n_values), linestyle='--', label="LL Insert Best Fit")
plt.plot(n_values, bt_insert_fit(n_values), linestyle='--', label="BST Insert Best Fit")

plt.xlabel("Number of Elements")
plt.ylabel("Time (seconds)")
plt.title("Insertion Time Comparison: Linked List vs BST")
plt.legend()
plt.grid()
plt.show()
