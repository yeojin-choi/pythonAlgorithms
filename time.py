## In this problem we count the number of times the number 3 appears from
## 00:00:00 to N:59:59

N = int(input("Enter the time: "))

hour=0
count=0

while hour<=N:
    minute = 0
    while minute<=59:
        second = 0
        while second <=59:
            time = str(hour)+str(minute)+str(second)
            if "3" in time:
                count+=1
            second+=1
        minute+=1
    hour+=1

print("The number three appears", count, "times.")

