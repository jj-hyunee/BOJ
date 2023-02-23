from collections import deque
N, K = map(int, input().split())
deq = deque()
res = []
for i in range(1, N + 1):
    deq.append(i)
while deq:
    for i in range(K-1):
        deq.append(deq.popleft())
    res.append(deq.popleft())

print("<", end='')
print(', '.join(map(str, res)), end='')
print(">", end='')