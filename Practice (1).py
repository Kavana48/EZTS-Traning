#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Context: A leading aerospace company, OrbitTech, is developing a satellite communication system that relies heavily on secure data transmission. The encryption keys used for securing communication between satellites and ground stations are generated based on prime numbers. To ensure the integrity and security of these keys, it is crucial to verify the primality of large numbers efficiently in real-time.
#Scenario: OrbitTech's satellite communication system requires real-time verification of prime numbers during the generation of encryption keys. Given the high-stakes nature of satellite data transmission, any delay or error in prime verification could compromise the security and efficiency of the system. Therefore, OrbitTech needs a reliable and efficient solution to check if given numbers are prime.

m = int(input("Enter the message: "))
flag = 0
if m<1:
    flag = 1
elif m == 1:
    flag = 0
else:
    for i in range(2,(m//2)+1):
        if m%i == 0:
            flag = 1
            break
    
if flag == 0:
    print("Valid Messgae")
else:
    print("invalid Message")


# In[ ]:


#Context: A financial services company, FutureInvest, uses advanced mathematical models to forecast market trends and make investment decisions. One of the models they use is based on the Fibonacci sequence due to its relevance in technical analysis, particularly in identifying retracement levels and predicting future price movements. Scenario: FutureInvest analysts need a reliable tool that can generate the Fibonacci sequence up to a specified number of terms. This tool will help them in creating Fibonacci retracement levels, which are critical for predicting potential reversal points in the financial markets. The accuracy and efficiency of generating these sequences are crucial for timely and effective decision-making.

n= int(input("Enter the no of terms: "))

a=0
b=1
c=a+b
if n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n):
        print(c)
        a=b
        b=c
        c=a+b


# In[ ]:


def check_prime(m):
    flag = 0
    if m<1:
        flag = 1
    elif m == 1:
        flag = 0
    else:
        for i in range(2,(m//2)+1):
            if m%i == 0:
                flag = 1
                break
    
    if flag == 0:
        return 1
    else:
        return 0

result=[]
N=int(input())
flag=0
k=N+1
while flag<1:
    flag = check_prime(k)
    if flag == 1:
        result.append(k)
    else:
        k=k+1

sum = 0
for i in range (N+1,k):
    sum+=i

result.append(sum)



p1=k
flag=0
k=p1+1
while flag<1:
    flag = check_prime(k)
    if flag == 1:
        p2=k
    else:
        k=k+1

p3=p1*p2
flag=check_prime(p3)
if flag == 0:
    result.append(False)
else:
    result.append(True)

Prime_key=tuple(result)

print(Prime_key)

