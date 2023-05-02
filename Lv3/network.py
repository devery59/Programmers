# idea : 방문 list를 만들어 check하고 시작 노드를 정해 해당 노드와 연결된 노드 모두 체크하도록 재귀 수행. visited가 전부 True일때까지 반복

def dfs(node, computers, visited):
    visited[node] = True
    for i, neighbor in enumerate(computers[node]):
        if neighbor > 0 and i != node and visited[i] == False:
            dfs(i, computers, visited)
    return visited


def solution(n, computers):
    answer = 1
    visited = [False] * n
    startNode = 0

    while True:
        visited = dfs(startNode, computers, visited)
        if False in visited:
            startNode = visited.index(False)
            answer += 1
        else:
            break

    return answer
