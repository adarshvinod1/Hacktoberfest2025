n=int(input())
a=0
for i in range(n):
    if i%2==0:
        for j in range(i+1):
            print(a+1,end="")
            if j<i:
                print("*",end="")
            a=a+1
        print("")
    else:
        s=a+i+1
        for j in range(i+1):
            print(s-j,end="")
            if j<i:
                print("*",end="")
            a=s
        print("")
