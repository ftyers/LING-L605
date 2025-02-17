from stack import Stack

a_stack = Stack(10)

print("Test push")

a_stack.push(11)
a_stack.push(3)
a_stack.push(4)
a_stack.push(38)

print("This is the stack now: ", a_stack.stack)

print("The peek shows: ", a_stack.peek())

a_stack.pop()
print("If we pop, we see: ", a_stack.stack)


