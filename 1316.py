# 1316
# 1. 각 단어를 리스트에 넣기(2차원으로 활용)
# 2. 0번째를 alpha에 넣은 후 비교
# 3. alpha[-1]이랑 1번째랑 비교 => 같으면 n+1이랑 비교(n은 1 ~ len(word[i]))
#                             / 다르면 alpha에 있는 알파벳인지 확인(in) 후 없으면 넣기(있으면 N-1 하고 다음 단어로)

N = int(input())
words = []

for _ in range(N):
    words.append(input())

for i in range(N):
    alpha = [words[i][0]]
    print("alpha: ", alpha)
    for j in range(len(words[i])):
        while words[i][j] != alpha[-1]:
            print(words[i][j], "!=", alpha[-1])
            if words[i][j] not in alpha:
                alpha.append(words[i][j])
                print("updated alpha = ", alpha, "\n")
            elif words[i][j] in alpha:
                N = N - 1
                print("***alpha = ", alpha, "\nN = ", N+1, " - 1 = ", N, "\n\n")
                break
print(N)

# 1. 각 단어를 set으로 중복 제거한 상태로 리스트에 넣기
# 2.


# N = int(input())
# result = N
#
# for _ in range(N):
#     word = input()
#     for j in range(len(word) - 1):
#         if word[j] == word[j+1]:
#             continue
#         elif word[j] in word[j+1:]:
#             result = result - 1
#             break
# print(result)