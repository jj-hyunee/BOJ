N, M = map(int, input().split())
graph = []
cnt = []
for _ in range(N):
    graph.append(input())

for i in range(N-7):
    for j in range(M-7):
        startW = 0
        startB = 0
        for w in range(i, i+8):
            for h in range(j, j+8):
                if (w+h) % 2 != 0:
                    if graph[w][h] != 'W':
                        startW += 1
                    else:
                        startB += 1
                else:
                    if graph[w][h] != 'W':
                        startB += 1
                    else:
                        startW += 1

        cnt.append(startW)
        cnt.append(startB)

print(min(cnt))
