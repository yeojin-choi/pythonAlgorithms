# Continue one of the two operations until N becomes 1:
# 1. Subtract 1 from N
# 2. Divided N by K (Only when it can be divided without a remainder)
# Write a program that counts the minimum number of operations.

N = int(input("Enter N: "))
K = int(input("Enter K: "))

count = 0

while N != 1:
    if (N % K != 0):
        N = N - 1
        count += 1
    else:
        N = N/K
        count += 1

if N == 1:
    print(count)

#-----------------------------------------------------------------------------------------------------------
# Another method with shorter runtime
# Problem with the previous code is that it has to iterate through all the subtract-ones
# Instead we could subtract a big number so that N is a multiple of K in one iteration.

N = int(input("Enter N: "))
K = int(input("Enter K: "))

count = 0
while (N != 1):
    targetNum = (N//K)*K
    count += (N-targetNum)
    N = targetNum/K
    count += 1

    if (N<K):
        count += N-1
        N = 1

print(int(count))


