a=list(map(int, input().split()))
maxi=-1
s=0
for i in a:
    s=s+i
    if s>maxi:
        maxi=5
print(maxi)