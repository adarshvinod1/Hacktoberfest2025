n= int(input())
for i in range(n):
    for k in range(n):
        if k+i<n-1:
            print(end=" ")
    for j in range(i+1):
        print(chr(j+65),end=" ")
    print("")
