import time
import random
import matplotlib.pyplot as plt
from LinkedList import LinkedList
from BinarySearchTree import BinarySearchTree

def compare_insertion():

    random.seed(42)
    num_values = 5000
    data = random.sample(range(1000, 20000), num_values)

    binarytree = BinarySearchTree()
    linkedlist = LinkedList()

    # track insert for binarytree
    track_time_tree = []
    initial_tree = time.time()
    for value in data:
        binarytree.insert(value)
        current = time.time()
        track_time_tree.append(current - initial_tree)

    # track append for linkedlist
    track_time_list_append = []
    initial_list_append = time.time()
    for value in data:
        linkedlist.append(value)
        current = time.time()
        track_time_list_append.append(current - initial_list_append)

    # track pretend for linked list
    track_time_list_prepend = []
    initial_list_prepend = time.time()
    for value in data:
        linkedlist.prepend(value)
        current = time.time()
        track_time_list_prepend.append(current - initial_list_prepend)

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.plot(track_time_tree, label="Binary Search Tree", color='b', linewidth=1.5)
    plt.plot(track_time_list_append, label="Linked List (Append)", color='r', linewidth=1.5)
    plt.plot(track_time_list_prepend, label="Linked List (Prepend)", color='g', linewidth=1.5)

    # Adjusting the x-axis for intervals of 500 bins
    plt.xticks(range(0, num_values, 500), rotation=45)

    plt.xlabel('Insertions')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Time for Insertions: Binary Tree vs Linked List')
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    compare_insertion()