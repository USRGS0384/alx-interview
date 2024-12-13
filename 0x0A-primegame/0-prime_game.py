#!/usr/bin/python3
"""
Prime Game: Maria and Ben play a game where they choose prime numbers
and remove them along with their multiples from the set.
The player who cannot make a move loses.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime number game after x rounds.

    Args:
        x (int): The number of rounds.
        nums (list of int): List of n values for each round.

    Returns:
        str or None: The name of the player with the most wins ('Maria' or 'Ben'),
        or None if there's a tie.
    """
    if x < 1 or not nums:
        return None

    def is_prime(n):
        """Check if a number is a prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sieve_of_eratosthenes(n):
        """Generate primes up to n using the Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_count = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

