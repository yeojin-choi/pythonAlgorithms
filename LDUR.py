N = input("Enter N: ")
plan = input("Enter the plan: ")
plan = plan.split()

x=1
y=1

for item in plan:
    if item == "L" and y!=1:
        y -= 1
    elif item == "R" and y!=N:
        y += 1
    elif item =="U" and x!=1:
        x -= 1
    elif item == "D" and x!=N:
        x += 1

print("The current position is (",x,",",y,")." )
