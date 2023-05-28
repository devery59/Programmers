# idea : 첫번째 집을 터냐 마냐의 문제로 가면 dp 로 귀결

def solution(money):
    d1, d2 = [0] * len(money), [0] * len(money)
    d1[0] = money[0]
    d1[1] = d1[0]

    # d1은 첫번째 집을 터는 경우
    for i in range(2, len(money) - 1):
        d1[i] = max(d1[i - 2] + money[i], d1[i - 1])

    # d2는 두번째 집을 터는 경우
    for i in range(1, len(money)):
        d2[i] = max(d2[i - 2] + money[i], d2[i - 1])
    return max(d1[-2], d2[-1])
