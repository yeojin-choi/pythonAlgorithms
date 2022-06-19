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