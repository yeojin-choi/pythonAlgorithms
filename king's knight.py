position = input("Enter the knight's current position: ")

def split(word):
    return [char for char in word]
position = split(position)
print(position)

alphabets = ["a","b","c","d","e","f","g","h"]
i=0
for alphabet in alphabets:
    if position[0] == alphabet:
        newpos = i
    i += 1
x=int(newpos)+1
y=int(position[1])

count=0
if x+2<9 and y+1<9:
    count +=1
if x+2<9 and y-1>0:
    count+=1
if x-2>0 and y+1<9:
    count+=1
if x-2>0 and y-1>0:
    count+=1
if y+2<9 and x+1<9:
    count +=1
if y+2<9 and x-1>0:
    count+=1
if y-2>0 and x+1<9:
    count+=1
if y-2>0 and x-1>0:
    count+=1


print("The number of ways this knight could move are",count)

