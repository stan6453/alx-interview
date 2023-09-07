#!/usr/bin/python3
"""Prime game module"""


def filterPrime(prime_nums):
    """Filter for prime numbers using the Sieve of Eratosthenes"""
    if len(prime_nums) < 3:
        return prime_nums
    prime_pointer = 0
    prime_veil = 2

    while prime_nums[prime_pointer] != 0:
        prime_num = prime_nums[prime_pointer]
        for index in range(prime_pointer+1, len(prime_nums)):
            if prime_nums[index] != 0 and prime_nums[index] % prime_num == 0:
                prime_nums[index] = 0
        if prime_nums[prime_veil] == 0:
            found_prime = False
            for index in range(prime_veil+1, len(prime_nums)):
                if prime_nums[index] != 0:
                    prime_nums[prime_veil] = prime_nums[index]
                    prime_nums[index] = 0
                    prime_veil += 1
                    found_prime = True
                    break
        if found_prime is False:
            break
        prime_pointer += 1
    return prime_nums[:prime_veil]


def pickWinner(nums, player1, player2):
    """Pick winner for the current round"""
    nums = filterPrime(nums)
    return player2 if len(nums) % 2 == 0 else player1


def isWinner(x, nums):
    """Return the winner of the prime game"""
    scores = {'Maria': 0, 'Ben': 0}
    if len(nums) == 0:
        return 'Ben'
    for index in range(min(x, len(nums))):
        winner = pickWinner(list(range(2, nums[index]+1)), 'Maria', 'Ben')
        scores[winner] += 1
    if scores['Maria'] > scores['Ben']:
        return 'Maria'
    if scores['Maria'] < scores['Ben']:
        return 'Ben'
    return None
