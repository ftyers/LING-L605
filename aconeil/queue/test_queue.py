from queue import Queue

q = Queue(5)

q.enqueue(15)

q.enqueue(14)
print(q)
q.enqueue(1)
q.enqueue(18)
print(q)
q.enqueue(6)

print("Is it full? ", q.full())
print(q)
print("Head is ", q.head())
print("Tail is ", q.tail())
print(q)
print("Removing one")
print(q.dequeue())
print(q)
print(len(q))
print("The tail is now ", q.tail())
print("Is it still full? ", q.full())
print("What about empty? ", q.empty())

p = Queue(5)

#p.enqueue(15)
p.enqueue(14)
p.enqueue(1)
p.enqueue(18)
p.enqueue(6)
print(p==q)
