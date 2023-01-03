# 4673
# 1. 1~1000까지 d(n) 연산을 진행
# 2. 연산을 통해 나온 값을 리스트에 넣기(중복 제거를 위해 set 사용)
# 3. 1~1000까지 돌면서 리스트에 없는 숫자로 리스트 만들어서 반환

# resultOfDN = set()
# selfNumber = set()
#
# for i in range(1, 10001):
#     resultOfDN.add(i + (i // 10000) + (i // 1000) + (i // 100) + (i // 10) + (i % 10))
#
# for j in range(1, 10001):
#     if j not in resultOfDN:
#         selfNumber.add(j)
#
# for selfNum in sorted(selfNumber):
#     print(selfNum)

resultOfDN = set()
selfNumber = set()

for i in range(1, 10001):
    resultOfDN.add(i + sum(map(int, str(i))))

for j in range(1, 10001):
    if j not in resultOfDN:
        selfNumber.add(j)

for selfNum in sorted(selfNumber):
    print(selfNum)