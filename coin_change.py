from typing import List


class Solution:
    @profile
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [10000 for _ in range(amount+1)]

        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:

                if coin <= i:

                    dp[i] = min(dp[i], 1 + dp[i-coin])

        if dp[-1] == 10000:
            return -1
        else:
            return dp[-1]


def main():
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    result = s.coinChange(coins, amount)
    print(result)


if __name__ == '__main__':
    main()
