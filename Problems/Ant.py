steps=int(input())
a=list(map(int,input().split()))
sp=0
ans=0
for i in a:
    sp=sp+i
    if sp==0:
        ans=ans+1
print(ans)