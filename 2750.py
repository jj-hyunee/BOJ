N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

res = sorted(numbers)
for j in res:
    print(j)