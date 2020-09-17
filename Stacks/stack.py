#stack = [3, 4, 5]
#stack.append(6)
#stack.append(7)
#print("First Edit")
#print(stack)
#stack.pop()
#print("Second Edit")
#print(stack)

from collections import deque

stack = deque()
stack.appendleft("test1")
stack.appendleft("test2")
print(stack)