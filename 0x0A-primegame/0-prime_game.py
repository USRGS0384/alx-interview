#!/usr/bin/python3
"""
Prime Game - determines the winner of the game
"""

def is_prime(n):
    """Returns True if n is a prime number, else False"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isWinner(x, nums):
    """
    Determines the winner of the game
    :param x: number of rounds
    :param nums: array of integers
    :return: name of the player that won the most rounds or None
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [i for i in range(1, n + 1) if is_prime(i)]
        maria_turn = True

        while primes:
            current_prime = primes.pop(0)
            primes = [p for p in primes if p % current_prime != 0]

            if maria_turn:
                if not primes:
                    maria_wins += 1
                maria_turn = False
            else:
                if not primes:
                    ben_wins += 1
                maria_turn = True

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    # Example usage
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))

