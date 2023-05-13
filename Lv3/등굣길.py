# idea : 고등학교 때 풀던 경우의수 찾기 문제. 가로 세로 첫줄을 1로 놓고 dp로 더해가면 된다.
# 기존에 쓰던 Index와 좌표 개념을 반대로하여 조금 헤맸다..


def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]  # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1  # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue
            if [i, j] in puddles:  # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:  # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n][m] % 1000000007
