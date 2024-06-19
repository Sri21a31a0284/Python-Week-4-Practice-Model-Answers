from collections import deque
n = int(input())
dq = deque()
for _ in range(n):
    input_str = input().split()
    op = input_str[0]
    if len(input_str) > 1:
        key = int(input_str[-1])
    match op:
        case "append":
            dq.append(key)
        case "appendleft":
            dq.appendleft(key)
        case "pop":
            dq.pop()
        case "popleft":
            dq.popleft()

print(*dq)
