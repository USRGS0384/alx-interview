#!/usr/bin/python3
""" Making changes """

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    :param coins: List[int] - List of the values of the coins
    :param total: int - The target total
    :return: int - Fewest number of coins needed, or -1 if not possible
    """
    if total <= 0:
        return 0
    
    # Initialize a DP array with a value greater than the maximum possible number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0
    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
