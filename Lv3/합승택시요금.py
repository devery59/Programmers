# idea : 플로이드 워셜 알고리즘을 이용하여 모든 지점 사이의 최소값을 갱신하고 각 지점까지 같이 타는 경우마다 체크하여 최소값을 최신화!

def solution(n, s, a, b, fares):
    INF = int(1e9)
    graphs = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graphs[i][i] = 0
    for fare in fares:
        start, end, cost = fare
        graphs[start][end] = cost
        graphs[end][start] = cost
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                graphs[j][k] = min(graphs[j][k], graphs[j][i] + graphs[i][k])
    answer = graphs[s][a] + graphs[s][b]
    for k in range(1, n + 1):
        answer = min(answer, graphs[s][k] + graphs[k][a] + graphs[k][b])
    return answer
