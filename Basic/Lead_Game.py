n = int(input())
p1 =0
p2 =0
d = 0
for i in range(n):
    n1,n2 = map(int, input().split())
    p1 +=n1
    p2+=n2
    diff = p1 - p2
    if diff>0 and diff > d:
        d = diff
        l =1 
    elif diff<0 and abs(diff)>d :
        d = abs(diff)
        l = 2  
print(l, d)
