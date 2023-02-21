##Ax - B(x-1) = V 식을 이용
A, B, V = list(map(int, input().split()))
where = 0
days = 0

while where < V:
    days = (V - B) / (A - B)
    if days == int(days):
        print(int(days))
        break
    else:
        print(int(days) + 1)
        break

##처음 썼던 코드
##이렇게 하면 시간이 너무 오래 걸림
A, B, V = list(map(int, input().split()))
where = 0
days = 0

while where < V:
    where = where + A
    if where >= V:
        days += 1
    else:
        where = where - B
        days += 1
        continue

print(days)