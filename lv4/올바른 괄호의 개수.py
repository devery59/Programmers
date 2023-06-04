# idea : 해당 문제는 카탈란 수를 활용하여 해결하는 문제이다
# 카랄란 수란 ? : 이진 트리의 수를 셀 때 활용하는 수열. (괄호 짝맞추기 문제, 정n다각형에 대각선을 그어 삼각형으로 분할하는 경우 등에 사용)
# 카랄란 수의 일반 점화식을 이용하여 접근하는 dp 문제


def solution(n):
    factorial = [1 for i in range(2 * n + 1)]

    for i in range(2, 2 * n + 1):
        factorial[i] = int(factorial[i - 1] * i)

    answer = int(factorial[2 * n] / (factorial[n] * factorial[n + 1]))

    return answer
