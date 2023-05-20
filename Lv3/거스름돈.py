# idea : 1원부터 n원까지 만들 수 있는 경우의 수를 dp로 만들어놓고 각 화폐단위만큼 건너뛰며 이전에 만들 수 있는 경우의 수에 더해준다.

DIV = 1_000_000_007


def solution(n, money):
    dp = [1] + [0] * n

    for coin in sorted(money):
        for price in range(coin, n+1):
            dp[price] = (dp[price] + dp[price - coin]) % DIV

    return dp[n]