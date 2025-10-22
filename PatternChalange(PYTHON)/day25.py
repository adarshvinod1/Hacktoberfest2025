n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print("")
for i in range(1,n):
    for j in range(n):
        if i+j<n:
            print("*",end="")
    print("")
        
