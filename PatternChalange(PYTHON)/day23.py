n=int(input())
for i in range(n):
    for j in range(n):
        if(j+i<=n-2):
            print(" ",end="")
    for j in range(-i,i+1):
        print(abs(j),end="")
    print("")
    
