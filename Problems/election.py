n=int(input())
arr=list(map(int,input().split()))
d={}
if n==1:
    print(arr[0])
else:
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
ans=-1
vals=list(d.items())
print(vals)
vals.sort(reverse=True, key=lambda x:x[1])
print(vals)
if len(vals)==1:
    ans=vals[0][0]
else:
    if vals[0][1]==vals[1][1]:
        ans=-1
    else:
        ans=vals[0][0]
print(ans)