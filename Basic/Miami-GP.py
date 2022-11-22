N=  int(input())
c1=0
c2=0
for i in range(N):
    X,Y = list(map(int, input().split()))
    c1=c1+X
    c2=c2+Y
    Z=X*107/100
    if(Y<=Z):
        print("YES")
    else:
        print("NO")
