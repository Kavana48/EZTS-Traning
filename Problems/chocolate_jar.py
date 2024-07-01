'''
jars=list(map(int,input().split()))
n=int(input())
a=0
for i in jars:
    print("This iteration is for ",i)
    a=a+i//3
    print(a)
    #remainder
    if i%3!=0:
        a+=1
    else:
        a+=0
    print(a)  
'''
    
jars=list(map(int,input().split()))
n=int(input())
a=0
for i in jars:
    a=a+(i//3)
    if(i%3==2 or i%3==1):
        a+=1
print(a)