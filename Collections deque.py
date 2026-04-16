
from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    command = input().split()
    method = command[0]
    if method == "append":
        d.append(command[1])
    elif method == "appendleft":
        d.appendleft(command[1])
    elif method == "pop":
        d.pop()
    elif method == "popleft":
        d.popleft()
print(*d)
