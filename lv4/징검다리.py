# idea : target으로 하는 최대 distance값을 이분법으로 구하는 방식으로 하여 접근.
# 어떤 돌을 제거해야하는지를 보는것이 아닌 해당 돌이 기준에 적합한지를 체크하는 방식.( 돌이 중심 X 목표로 하는 값이 중심 O)


def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.append(distance)
    rocks.sort()

    while left <= right:
        mid = (left + right) // 2
        current, remove = 0, 0
        min_distance = float('inf')

        for rock in rocks:
            dis = rock - current
            if dis < mid:
                remove += 1
            else:
                current = rock
                min_distance = min(min_distance, dis)

        if remove > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer
