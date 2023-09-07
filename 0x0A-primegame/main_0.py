#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


#Maria wins
print("Winner: {}".format(isWinner(3, [5, 5, 1])))
print("Winner: {}".format(isWinner(1, [2])))


#Ben wins
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(1, [1])))

#None
print("Winner: {}".format(isWinner(4, [2, 3, 5, 10])))

