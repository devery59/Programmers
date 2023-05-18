# idea : 배열 양쪽에서 체크했을때의 최소값 중 자신보다 하나라도 큰게 있다면 무조건 살아남을 수 있음.
# 양쪽의 최소값들이 나머지를 전부 터뜨려주고 양쪽 최소값중 작은 놈만 터뜨리면 되기 때문

def solution(a):
    result = [False] * len(a)
    minFront, minRear = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True
    return sum(result)