n=int(input())
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    if i==0 or i==n-1:
         for y in range(2*i+1):
             print("*",end="")
    else:
        print("*",end="")
        for z in range(2*i-1):
            print(" ",end="")
        print("*",end="")
    print()
    