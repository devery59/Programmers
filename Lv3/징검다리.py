# idea : 최대값이 1억 이상인 것은 보고 이분탐색 문제라고 생각. left right 중간값이 연속해서 k개 나타나면 불가능한 경우이므로 줄이고 아니라면 증가

def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left