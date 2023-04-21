# idea : 맨 위부터 시작하여 아래로 내려가면서 바로 수를 누적해서 더해 현재 위치에 다다를 수 있는 경로중 최대값과 현재 위치 값을 더한다.
# new knowledge : enumerate -> list에서 index와 값을 뽑아주는 함수. dict 에서 key value 뽑는것처럼 사용
def solution(triangle):
    graph = [[] for _ in range(len(triangle))] # 누적된 결과를 저장하기 위한 Adjacency Matrix
    for index, values in enumerate(triangle): # triangle array에서 값을 하나씩 추출하여 이전 경로까지의 최대값과 더하기
        for i, value in enumerate(values):
            if index == 0:
                graph[index].append(value)
            else:
                if i == 0:
                    graph[index].append(graph[index - 1][i] + value)
                elif i == len(values) - 1:
                    graph[index].append(graph[index - 1][i - 1] + value)
                else:
                    graph[index].append(max(graph[index - 1][i - 1], graph[index - 1][i]) + value)
    # 맨 마지막 list 값은 전체의 누적 값이므로 해당 리스트에서의 최대값을 추출
    answer = max(graph[len(graph) - 1])

    return answer
