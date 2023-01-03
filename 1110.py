# 1110  더하기 사이클 (구현)
# 1. 새로운 수는 N의 1의 자리가 10의 자리가 되고/ N의 10의 자리와 1의 자리를 더한 수의 1의 자리가 새로운 수의 1의 자리가 됨
# 2. 함수에서 나온 결과값과 주어진 N 비교 => cnt 로 사이클 숫자 세기

N = int(input())
cnt = 0
newN = N

while True:
    a = newN % 10  # N의 1의 자리 (6)
    b = newN // 10  # N의 10의 자리 (2)
    c = (a + b) % 10  # N의 10의 자리와 1의 자리를 더한 수의 1의 자리 (8)
    newN = int(str(a) + str(c))
    cnt += 1
    if newN == N:
        break

print(cnt)
