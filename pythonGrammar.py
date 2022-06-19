# addition
# 0.3+0.6 = 0.8999999 in python

a = 0.3+0.6

print(round(a,4)) #넷째자리에서 셋째자리가지 반올림

a=7
b=3

print(a/b)
print(a%b)
print(a//b)
print(a**b)

# List
a = [1,2,3,4]
print(a[4])

a = list() #empty list
print(a)

a=[] #empty list
print(a)

a = [0]*10
#[0,0,0,0,0,0,00,0,0]
print(a)

#List comprehension
array = [i for i in range(20) if i%2==1]
print(array)

array = [i*i for i in range(1,10)]
print(array)

#2D array of dimension NxM
n=3
m=4
array = [[0]*m for _ in range(n)]

#don't do this
array = [[0]*m]*n
print(array)

#list methods
a= [1,4,3]
a.append(5)
a.sort() #오름차순
a.sort(reverse = True) #내림차순
a.reverse()
a.insert(2,3)
a.count(3)
a.remove(1)

#strings
data = "Hello World"
print(data)

print("Don't you know\"python\"?")

a = "string"
print(a*3)

a = "abcdef"
print(a[2:4])

#tuple
#List: []
#Tuple: ()
a = (1,2,3,4)
a[2] = 7
#this is impossible

#DICTIONARIES
data = dict()
data['사과']='Apple'
data['바나나']='Banana'
data['키위']='Kiwi'
#dictionaries are good because they take up less space. for example, if you have to mark 10,000 samples out of 100,000,
#90,000 of them won't be used if we create a separate list. However if we use a dictionary that inefficiencty is reduced.
if '사과'in data:
    print("사과를 키로 갖는 데이터가 존재합니다")

key_list = data.keys()
value_list = data.values()
for key in key_list:
    print(data[key])

#SETS
# 1. no overlaps
# 2. no order
# 3. no keys, only values
data = set([1,2,3,4,5,5,5]) #={1,2,3,4,5}
data = {1,1,2,3,4,4,5} #={1,2,3,4,5}

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print(a|b) #합집합
print(a&b) #교집합
print(a-b) #차집합

data = set([1,2,3])
data.add(4)
data.update(5,6) #adding multiple values
data.remove(3)
