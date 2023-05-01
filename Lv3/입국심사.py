# idea : 이분탐색 문제이므로 최소, 최대 범위를 정하고, 중간값으로 처리하는 사람 수를 연산하여 n명보다 많아지는 시점을 구한다

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n  # 가장 비효율적인 경우는 times에서 제일 오래 걸리는 사람이 n명을 모두 처리하는 것
    while left <= right:  # 둘의 관계가 역전된 순간에 stop!
        mid = (left + right) // 2
        process_amount = 0
        for time in times:
            process_amount += mid // time
            if process_amount >= n:  # 이미 n명 이상 처리할 수 있는 경우
                break
        if process_amount >= n:  # 최적값보다 mid가 큰경우
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
