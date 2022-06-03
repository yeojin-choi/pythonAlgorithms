# There are N x M number cards in N rows and M columns.
# First choose the row that you will be selecting the cards from.
# And then from the row chosen, you have to choose the smallest card.
# That card has to be the highest card among all options.
# input example:
# 3 3 (each n and m)
# 3 1 2
# 4 1 4
# 2 2 2
# Output example: 2


n, m = map(int, input("Enter n and m: ").split())
# What is a map function?
# https://tutorial.eyehunts.com/python/python-map-function-data-structure-example/
# Python map function or map data structure implements a given function
# to each item of an iterable (list, tuple, etc.) and returns a list of the results.

result = 0
for i in range(n): # range(n) is 0 ~ n-1
    row = list(map(int, input("Enter row: ").split())) # save row as a list
    minimum = min(row)
    result = max(minimum, result)

print(result)
