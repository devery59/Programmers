# idea : 마지막에 돌 하나가 남는 경우에는 +1, 두개가 남으면 +2 한다고 생각하면 dp 문제로 귀결

def solution(n):
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 2001):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567
