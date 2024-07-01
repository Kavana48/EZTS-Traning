#!/usr/bin/env python
# coding: utf-8

# In[ ]:


S= input()
dic = {'A':0,'E':0,'I':0,'O':0,'U':0}
for i in S:
    if i == 'a' or i == 'A':
        dic['A'] += 1
    elif i == 'e' or i == 'E':
        dic['E'] += 1
    elif i == 'i' or i == 'I':
        dic['I'] += 1
    elif i == 'o' or i == 'O':
        dic['O'] += 1
    elif i == 'u' or i == 'U':
        dic['U'] += 1

x=max(dic.values())
result =[]
for i,j in dic.items():
    if j == x:
        result.append(i)

print(result)




# In[ ]:


def count_vowel(S):
    dic = {'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in S:
        if i == 'a' or i == 'A':
            dic['A'] += 1
        elif i == 'e' or i == 'E':
            dic['E'] += 1
        elif i == 'i' or i == 'I':
            dic['I'] += 1
        elif i == 'o' or i == 'O':
            dic['O'] += 1
        elif i == 'u' or i == 'U':
            dic['U'] += 1
    
    x=max(dic.values())
    result =[]
    for i,j in dic.items():
        if j == x:
            result.append(i)
    
    return result



i_p = [
    ["Alex", "I enjoy hiking in the mountains."],
    ["Sam", "A lovely sunny day at the beach."],
    ["Jamie", "Reading a book is my favorite pastime."],
    ["Taylor", "I love playing video games on weekends."],
    ["Chris", "Exploring new cities is exciting and fun."]
]

o_p = {}

for i in i_p:
    o_p[i[0]]= count_vowel(i[1])

print(o_p)


# In[ ]:


sample input [2,4,3,5,6,3,4,6,7,1,2,5]

output: [4,6,7]

l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum = max = 0
for i in range(0,len(l)-2):
    sum = l[i]+l[i+1]+l[i+2]
    if max<sum:
        max = sum
        pos=i

print(max,l[pos],l[pos+1],l[pos+2])




# In[ ]:


l=[2,4,3,5,6,3,4,6,7,9,9,9]
window = max = 0
k = int(input("Enter the no of continious digit: "))

for j in range(0,k):
        window+=l[j]
l.append(0)
for i in range(0,len(l)-k):
    if max<window:
        max=window
        pos=i
    window = window+l[i+k]-l[i]

print("result")
print(max)
for j in range(0,k):
    print(l[pos+j])

