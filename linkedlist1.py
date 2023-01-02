from collections import deque

queue = deque()

for i in range(5):
    queue.append(i)
    print(queue)

for i in range(0,5):
    queue.popleft()
    print(queue)

stack = deque()

for i in range(5):
    stack.append(i)
    print(stack)

for i in range(5):
    stack.pop()
    print(stack)