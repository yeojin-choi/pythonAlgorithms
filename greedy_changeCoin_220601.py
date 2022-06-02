# This is a Greedy algorithm
# Question:
# If you have to give N won of change, what is the minimum number of coins
# that you can give them? (N is always a multiple of 10)
# Korean won coins are 500 won, 100 won, 50 won, and 10 won.

# Thought process:
# Always start with the biggest coin using the mod function

n = 1260 # n is the number of money
coins = [500,100,50,10]
count = 0

for coin in coins:
    count += n//coin # count the number of each coin
    n %= coin # update n with the remainder

print(count)

# Time complexity: O(4) because there are four types of coins
