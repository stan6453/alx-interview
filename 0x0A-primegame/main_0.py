#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

# Maria wins
print("Winner: {}".format(isWinner(3, [5, 5, 1])))
print("Winner: {}".format(isWinner(1, [2])))
print("Winner: {}".format(isWinner(3, [0, 11, 11])))

print('')

# Ben wins
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(1, [1])))
print("Winner: {}".format(isWinner(1, [0])))
print("Winner: {}".format(isWinner(3, [0, 0, 0])))
print("Winner: {}".format(isWinner(5, [1, 1, 1, 1, 1])))

print('')

# None
print("Winner: {}".format(isWinner(4, [2, 3, 5, 10])))
print("Winner: {}".format(isWinner(6, [0, 0, 0, 11,11,11])))


print("Winner: {}".format(isWinner(2, [0, 0, 0, 11,11,11])))

print('')



