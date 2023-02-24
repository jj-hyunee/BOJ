A = int(input())
for _ in range(A):
    answer = []
    N, M = list(map(int, input().split()))
    importance = list(map(int, input().split()))
    numLst = list(range(len(importance)))
    numLst[M] = '!'
    order = 0
    while True:
        if importance[0] == max(importance):
            order += 1
            if numLst[0] == '!':
                print(order)
                break
            else:
                importance.pop(0)
                numLst.pop(0)
        else:
            importance.append(importance.pop(0))
            numLst.append(numLst.pop(0))