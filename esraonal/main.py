import time
import random
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from linkedlist import LinkedList
from binarysearchtree import BinarySearchTree
from heap import Heap

def compare_insertion():
    random.seed(42)
    num_values = 5000
    data = random.sample(range(1000, 20000), num_values)

    binarytree = BinarySearchTree()
    linkedlist = LinkedList()
    heap = Heap()

    # track insert for binarytree
    track_time_tree = [0]
    initial_tree = time.time()
    for value in data:
        binarytree.insert(value)
        current = time.time()
        track_time_tree.append(current - initial_tree)

    # track append for linkedlist
    track_time_list_append = [0]
    initial_list_append = time.time()
    for value in data:
        linkedlist.append(value)
        current = time.time()
        track_time_list_append.append(current - initial_list_append)

    # track pretend for linked list
    track_time_list_prepend = [0]
    initial_list_prepend = time.time()
    for value in data:
        linkedlist.prepend(value)
        current = time.time()
        track_time_list_prepend.append(current - initial_list_prepend)

    # track insert for heap
    track_time_heap_insertion = [0]
    initial_heap_insertion= time.time()
    for value in data:
        heap.insert(value)
        current = time.time()
        track_time_heap_insertion.append(current - initial_heap_insertion)

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.plot(track_time_tree, label="Binary Search Tree", color='b', linewidth=1.5)
    plt.plot(track_time_list_append, label="Linked List (Append)", color='r', linewidth=1.5)
    plt.plot(track_time_list_prepend, label="Linked List (Prepend)", color='g', linewidth=1.5)
    plt.plot(track_time_heap_insertion, label="Heap", color='y', linewidth=1.5)

    # Adjusting the x-axis for intervals of 500 bins
    plt.xticks(range(0, num_values, 500), rotation=45)

    # Use logarithmic scale for y-axis to enhance visibility of small values
    plt.yscale('log')

    plt.xlabel('Insertions')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Time for Insertions: Binary Tree vs Linked List vs Heap')
    plt.legend()
    plt.grid(True)

    plt.show()
    
def compare_deletion():
    random.seed(42)
    num_values = 5000
    data = random.sample(range(1000, 20000), num_values)

    binarytree = BinarySearchTree()
    linkedlist = LinkedList()

    for value in data:
        binarytree.insert(value)
        linkedlist.append(value)

    # track deletion for Binary Search Tree
    track_time_tree = [0]
    initial_tree = time.time()
    for value in data:
        binarytree.delete(value)
        current = time.time()
        track_time_tree.append(current - initial_tree)

    # track deletion for Linked List
    track_time_list = [0]
    initial_list = time.time()
    for value in data:
        linkedlist.delete(0)  
        current = time.time()
        track_time_list.append(time.time() - initial_list)

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.plot(track_time_tree, label="Binary Search Tree Deletion", color='b', linewidth=1.5)
    plt.plot(track_time_list, label="Linked List Deletion", color='r', linewidth=1.5)

    # Adjusting the x-axis for intervals of 500 bins
    plt.xticks(range(0, num_values, 500), rotation=45)

    plt.xlabel('Deletions')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Time for Deletion: Binary Tree vs Linked List')
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    compare_insertion()
    # compare_deletion()