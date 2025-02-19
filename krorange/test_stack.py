from stack import Stack

mystack = Stack(5)
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)

print(mystack.stack)

val = mystack.pop()
print(val)
print(mystack.stack)

val = mystack.pop()
print(val)
print(mystack.stack)

# test __eq__
s1 = Stack(5)
s2 = Stack(5)

s1.push(1)
s1.push(2)
s2.push(1)
s2.push(3)

print(s1, s2)
print("Is it equal?")
print(s1 == s2)

v = s2.pop()
s2.push(2)

print(s1, s2)
print("Is it equal?")
print(s1 == s2)

# test __len__
print("The length of s1:")
print(len(s1))
print("The length of s2:")
print(len(s2))

# test __contains__
s1 = Stack(5)
s2 = Stack(5)

s1.push(1)
s1.push(2)
s2.push(1)
s2.push(3)

print(s1, s2)
print("Is 3 in s1?")
print(3 in s1)
print("Is 3 in s2?")
print(3 in s2)