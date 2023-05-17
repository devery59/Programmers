# idea : 순위를 고려할 때는 승패의 정보 모두가 필요하니 때문에 두가지 정보를 모두 조합하여 관리. 한 사람이 이기고 진 결과 개수가 n-1인 경우만 카운트

from collections import defaultdict


def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)  # key 가 value 한테 이겼다
    lose_graph = defaultdict(set)  # key 가 value 한테 졌다

    for winner, loser in results:
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)

    for i in range(1, n + 1):
        for winner in win_graph[i]:  # i한테 진 애들은 i를 이긴 애들한테도 진 것
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:  # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
            win_graph[loser].update(win_graph[i])

    for i in range(1, n + 1):
        if len(win_graph[i]) + len(lose_graph[i]) == n - 1:
            answer += 1

    return answer
