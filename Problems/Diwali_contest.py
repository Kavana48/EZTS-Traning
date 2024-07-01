probs=int(input())
tot=int(input())
c=0
s=0
rt=4*60-tot

#logic 1
for i in range(1,probs+1):
    s=s+5*i
    if s>rt:
        break
    c=c+1
print(c)

#logic 2
for i in range(1,probs+1):
    if s<rt:
        s=s+5*i
        c=c+1
print(c)