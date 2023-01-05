# 1316
# 1. isGroupWord 함수는 각 알파벳이 오른쪽에 있는 알파벳과 같으면 넘어가고 같지 않으면 그 오른쪽에 있는 단어를 a 리스트에 append 한다
# 2. 각 단어를 set() 에 넣어서 중복을 제거하고, isGroupWord를 통해 얻은 a와 길이가 같으면 cnt를 1 더한다
# 3. 마지막으로 그룹단어인 수(cnt)만 출력하면 된다.
N = int(input())
cnt = 0


def isGroupWord(word):
    a = []
    a.append(word[0])
    if len(word) == 1:
        a = a
    else:
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                continue
            else:
                a.append(word[i + 1])
    return a


for _ in range(N):
    inputWord = input()
    if len(set(inputWord)) == len(isGroupWord(inputWord)):
        cnt += 1

print(cnt)
