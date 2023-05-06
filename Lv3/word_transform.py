# idea : deque를 선언해놓고 1개의 알파벳만 다른 경우의 단어를 모두 deque에 추가해가며 비교하면서 진행

from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visited = [False] * len(words)
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = True

    return answer
