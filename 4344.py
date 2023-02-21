C = int(input())

for _ in range(C):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
    result = (cnt / scores[0]) * 100
    print(f'{result:.3f}%')
##round(result, 3)을 썼더니 40.0%는 소숫점 이후 세자리로 나오지 않음