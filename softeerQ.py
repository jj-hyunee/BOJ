### 금고 털이
# W, N = map(int, input().split())
# jewelss = []
# for _ in range(N):
#     jewels = list(map(int, input().split()))
#     jewelss.append(jewels)
#
# sortedJewels = sorted(jewelss, key = lambda x : x[1], reverse=True)
# # print(sortedJewels)
#
# resultPrice = 0
# for weight, price in sortedJewels:
#     if W > weight:
#         resultPrice += weight * price
#         W -= weight
#     else:
#         resultPrice += W * price
#         break
# print(resultPrice)

### 8단 변속기
import sys
input = sys.stdin.readline
speed = list(map(int, input().split()))

speedA = sorted(speed)
speedD = sorted(speed, reverse=True)

if speed == speedA:
    print("ascending")
elif speed == speedD:
    print("descending")
else:
    print("mixed")