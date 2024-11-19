limt=int(input("Enter the Limit:"))
for i in range(limt):
    for j in range(i):
        print("*",end=" ")
    print()
limit_2=int(input("Enter the limit 2:"))
for i in range(limit_2,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
limit_3=int(input("Enter the limit 3:"))
for i in range(1,limit_3 + 1):
    for j in range(limit_3-i):
        print(" ", end=" ")
    for k in range(2*i - 1):
        print("*", end=" ")
    print()
limit_4=int(input("Enter the limit 4:"))
for i in range(limit_4,0,-1):
    for j in range(limit_3-i,):
        print(" ", end=" ")
    for k in range(2*i - 1):
        print("*", end=" ")
    print()
