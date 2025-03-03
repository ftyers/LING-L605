import time
import binary_search_tree.bst
import linked_list.ll
import random
import matplotlib.pyplot as plt
import heap.heap

random.seed(42)
bt = binary_search_tree.bst.BinarySearchTree()
ll = linked_list.ll.LinkedList()
hp = heap.heap.Heap()

#make random lists of integers
list_len = [100,500,1000,2000,3000,4000,5000]#,6000,7000,8000,9000,10000]
data = []
for length in list_len:
    new_list = []
    for i in range(0, length):
        new_list.append(random.randint(0,100))
    data.append(new_list)

btb_yvalue = []
btb_xvalue = []
for d in data:
    btb = time.time()
    for num in d:
        bt.insert(num)
    bte = time.time()
    btb_xvalue.append(len(d))
    btb_yvalue.append(bte-btb)
    print(len(d), "took ", bte-btb, "for bst")

heap_yvalue = []
heap_xvalue = []
for d in data:
    heapb = time.time()
    for num in d:
        bt.insert(num)
    heape = time.time()
    heap_xvalue.append(len(d))
    heap_yvalue.append(heape-heapb)
    print(len(d), "took ", heape-heapb, "for bst")


llb_yvalue = []
llb_xvalue = []
for d in data:
    llb = time.time()
    for num in d:
        ll.prepend(num)
    lle = time.time()
    llb_yvalue.append(lle-llb)
    llb_xvalue.append(len(d))
    print(len(d), "took ", lle-llb, "for ll")

plt.plot(llb_xvalue, llb_yvalue, label="Linked List")
plt.plot(btb_xvalue, btb_yvalue, label="Binary Search Tree")
plt.plot(heap_xvalue, heap_yvalue, label="Heap")
plt.legend()
plt.xlabel("Length of list")
plt.ylabel("Program run time")
plt.title("Insertion time")
plt.show()
