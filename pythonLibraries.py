#internal functions in python
sum([1,2,3,4,5])
min(7,3,5,2)
max(7,3,5,2)
eval("(3+5)*7") #수식의 결과를 반환
sorted([9,1,8,5,4])
sorted([9,1,8,5,4], reverse=True)
sorted([('tom',15),('nam',17),('cruise',19)],key=lambda x:x[1], reverse=True) #sort by second element of tuple

data = [9,1,2,3,4]
data.sort()
print(data)

#ITERTOOLS
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3))
print(result)

from itertools import combinations
data = ['A','B','C']
result = list(combinations(data,2))
print(result)

from itertools import product
data = ['A','B','C']
result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

from itertools import combinations_with_replacement
data = ['A','B','C'] #데이터 준비
result = list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)


