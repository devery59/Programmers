# idea: stations가 오름차순으로 제공되기 때문에 시작점으로부터 기지국 위치를 하나씩 받으며 해당 구간에 필요한 최소 개수 더하기

from math import ceil


def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1  # cover range

    start = 1
    for s in stations:
        answer += max(ceil((s - w - start) / W), 0)  # add only start is less than current station
        start = s + w + 1

    if n >= start:  # stations에서 받은 마지막 기지국이 전체 길이보다 작을 경우
        answer += ceil((n - start + 1) / W)

    return answer
