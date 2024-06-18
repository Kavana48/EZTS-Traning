#!/usr/bin/env python
# coding: utf-8

# ### chocolate
# You are given an integer array of size N, representing jars of chocolates. Three
# students A, B, and C respectively, will pick chocolates one by one from each chocolate
# jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task
# is to fine and return an integer value representing the total number of chocolates that
# student A will have, after all the chocolates have been picked from all the jars.
# Note: Once a jar is done A will start taking the chocolates from the new jar.
# Input Format :
# input1: An integer array representing the quantity of chocolates in each jar.
# input2: An integer value N representing the number of jars.
# Output Format:
# Return an integer value representing the total number of chocolates that student A
# will have, after all the chocolates are picked.
# Example:
# Input:
# 10 20 30
# 

# In[ ]:


arr=list(map(int,input().split()))
n=int(input())
c=0
for i in arr:
    if i==0:
        continue
    if(i<=3):
        c=c+1
    else:
        if(i%3==0):
            c=c+i//3
        else:
            c=c+i//3+1
print(c)     


# ### 2nd problem sloving

# In[ ]:


arr=list(map(int,input().split()))
n=int(input())
c=0
for i in arr:
    if i==0:
        continue
    if(i<=n):
        c=c+1
    else:
        if(i%n==0):
            c=c+i//3
        else:
            c=c+i//n+1 #c =students
print(c)     


# ### DOG AGE'''
# Max is having a dog . he want  to find the age of the dog  with respect to the age of human.
# he came to know that , the age of the  dog is mesured with respect to human  has a formula to proceed. 
# example: 1 year of life span of dog is same as seveen years of  life span  of human being
# Now , calculate the age of MAX dog.
# '''

# In[23]:


def dog_age(n):
    return n*7
n=int(input())
print(dog_age(n))


# In[ ]:


arr=list(map(int,input().split()))
n=int(input())
c=0
for i in arr:
    if i==0:
        continue
    if(i<=n):
        c=c+1
    else:
        if(i%n==0):
            c=c+i//3
        else:
            c=c+i//n+1 #c =students #this for A only
print(c)     


# In[ ]:





# ### Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8
# PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the
# party venue within this time which takes him P minutes. The contest comprises
# of N problems that are arranged in order of difficulty, with problem 1 being the
# simplest and problem N being the most difficult. Max is aware that he will require 5*i
# minutes to solve the ith problem.
# Your task is help Max find and return an integer value, representing the number of
# problems Max can solve and reach the party venue within the given time frame of 4
# hours.
# Note: Max will leave his home at exactly 8 PM to reach the party venue.
# Input Format:
# input1: An integer value N, representing the total number of problems.
# input2: An integer value P, Representing the time to travel in minutes from his home
# to the party venue.

# In[ ]:


def max_problems_to_solve(N, P):
    time_left = 240 - P  # 4 hours in minutes minus travel time
    problems_solved = 0
    for i in range(1, N + 1):
        time_needed = 5 * i  # Time needed to solve ith problem
        if time_needed <= time_left:
            problems_solved += 1
            time_left -= time_needed
        else:
            break
    return problems_solved

# Example usage:
N = int(input("problem to be soloved"))
P = int(input("time to solove"))
print(max_problems_to_solve(N, P))


# In[ ]:


N = int(input("problem to be soloved"))
P = int(input("time to solove")) #p=time nd the time man wasted so -minus
print(problems_solve(N, P))
def problem_solve(N,1):
    time = 240-p
    problems = 0
    for i in range(1,N+1):
        time_need=5*i
        if time_needed<=time+left:
            problem_soloved+=1
            time_left-=time_needed
        else:
            break
        return problem_soloved  
            


# ### space count
# 

# In[15]:


n=input("enter the sentence : ")
count=0
for char in n:
    if char==' ':
        count=count+1
print(count)        
        


# In[ ]:





# ### Paul is given an array A of length N. He must perform the following Operations on the
# array sequentially:
# * Choose any two integers from the array and calculate their average.
# * If an element is less than the average, update it to 0. However, if the element is
# greater than or equal to the average, he need not update it.
# Your task is to help Paul find and return an integer value, representing the minimum
# possible sum of all the elements in the array by performing the above operations. Note: An exact average should be calculated, even if it results in a decimal.
# Input Format:
# input1: An integer value N, representing the size of the array A.
# input2: An integer array A.
# Output Format:
# Return an integer value, representing the minimum possible sum of all the elements
# in the array by
# Sample Input
# 5
# 1 2 3 4 5
# Sample Output
# 5
# #by sorting

# ### DAY 5 PROBLEM SOLVING

# ###  accenture question The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i
# 
# Note:
# 
# Return -1 if the array is null
# Return 0 if the total amount of food from all houses is not sufficient for all the rats.
# Computed values lie within the integer range.
# Example:
# 
# Input:
# 
# r: 7
# unit: 2
# n: 8
# arr: 2 8 3 5 7 4 1 2
# Output:
# 
# 4
# 
# Explanation:
# Total amount of food required for all rats = r * unit
# 
# = 7 * 2 = 14.
# 
# The amount of food in 1st houses = 2+8+3+5 = 18. Since, amount of food in 1st 4 houses is sufficient for all the rats. Thus, output is 4.

# In[6]:


def calculate_food(r,unit,arr):#arr =amt of stored food in house  
    total_food_required =  r*unit
    total_food_available= sum(arr)
    #sum of the elements in the array
    for  i in arr:
        
        if arr ==0:
            return -1
        else:
            if total_food_available < total_food_required:
                return 0
            else:
                return "none"
      
    
r=int(input("enter the number of rats :"))
unit=int(input("enter the food :"))
arr=list(map(int,input().split( )))
print(calculate_food(r,unit,arr))


# In[7]:


def ant(r,unit,arr):
    if len(arr)==0:
        return -1
    total_food_req=r*unit
    total_food_available=sum(arr)
    if(total_food_available<total_food_req):
        return 0
    else:
        return -1
r=int(input("enter the number of rats :"))
unit=int(input("enter the food :"))
arr=list(map(int,input().split( )))
print(ant(r,unit,arr))


# #### The Binary number system only uses two digits, 0 and 1 and number system can be called binary string. You are required to implement the following function:
# int OperationsBinaryString(char* str);
# 
# The function accepts a string str as its argument. The string str consists of binary digits eparated with an alphabet as follows:
# 
# – A denotes AND operation – B denotes OR operation – C denotes XOR Operation You are required to calculate the result of the string str, scanning the string to right taking one opearation at a time, and return the same.
# 
# Note:
# 
# No order of priorities of operations is required Length of str is odd If str is NULL or None (in case of Python), return -1 Input: str: 1C0C1C1A0B1
# 
# Output: 1
# 
# Explanation: The alphabets in str when expanded becomes “1 XOR 0 XOR 1 XOR 1 AND 0 OR 1”, result of the expression becomes 1, hence 1 is returned.
# 
# Sample Input: 0C1A1B1C1C1B0A0
# 
# Output: 0

# In[17]:


def OperationsBinaryString(str):
    a=int(str[0]) #indexing
    i=1
    while(i<len(str)):
        if(str[i]=="A"):
            a=a&int(str[i+1])
        elif(str[i]=="B"):
            a=a|int(str[i+1])   
        else:
            a=a^int(str[i+1])
        i=i+2
    return a
str=input()
print(OperationsBinaryString(str))


# You are given a function.
# int CheckPassword(char str[], int n);
# The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
# str is a valid password if it satisfies the below conditions.
# 
# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash (/)
# – Starting character must not be a number
# Assumption:
# Input string will not be empty.
# 
# Example:
# 
# Input 1:
# aA1_67
# Input 2:
# a987 abC012
# 
# Output 1:
# 1
# Output 2:
# 0### 

# In[36]:


def CheckPassword(str):
    if len(str)<4:
        return 0
    if not any(char.isdigit() for char in str):
               return 0
    if not any(char.isupper() for char in str):
               return 0
    if ' ' in str or '/' in str:
               return 0
               return 1


print(CheckPassword("aA1_67")) 
print(CheckPassword("a987 abC012"))
        


# In[ ]:


def calculate_final_score(s):
    score = 0
    consecutive_heads = 0
    
    for result in s:
        if result == 'H':
            score += 2
            consecutive_heads += 1
            if consecutive_heads == 3:
                break
        elif result == 'T':
            score -= 1
            consecutive_heads = 0
    
    return score

# Example usage:
s = "HHHTT"
print(calculate_final_score(s))  # Output: 6


# In[38]:


def CheckPassword(str,n):
    if n<4:
        return 0
    if str[0].isdigit():
        return 0
    caps =0
    nums=0
    for i in str:
        if(str[i]==" " or str[i]=="/"):
            return 0
        if(str[i]>'A' or str[i]=='Z'):
            caps+=1
        elif str[i].isdigit():
            nums+=1
        if caps>0 and nums>0:
            return 1
        else:
            return 0
        


# ### You are given a function,
# int findCount(int arr[], int length, int num, int diff);
# 
# The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
# Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.
# 
# Example:
# Input:
# 
# arr: 12 3 14 56 77 13
# 
# num: 13
# 
# diff: 2
# 
# Output:
# 3
# 
# Explanation:
# Elements of ‘arr’ having absolute difference of less than or equal to ‘diff’ i.e. 2 with ‘num’ i.e. 13 are 12, 13 and 14.

# In[4]:


def findCount(arr, num, diff):
    count = 0
    
    for i in range(len(arr)):
        if(abs(arr[i]-num)<=diff):
            count+=1
    return count
        
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(findCount(arr, num, diff))


# ### 
# Toss and score
# You are playing a game of Toss and Score in the Hillwood City Mall with your friends.
# The game consists of the following rules:
# Toss an unbiased coin multiple times.
# For each heads you get 2 points and for each tails you lose 1 point.
# The game ends as soon as you get 3 heads in a row, or you toss the coin throughout
# the length of string S.
# You have been given a string 5 consisting of letters H (for heads) and T (for tails)
# denoting the sequence results you get on the tass of coin N times. Your task is to find
# and return an integer value representing the final score you get once the game ends.
# Note: The final score can be negative too.
# Input Specification:
# Input1: A string s. representing the sequence of results you get on the toss of coin N times
# Sample Input:
# HHHTT
# Output:
# 6
# '''

# In[3]:


def calculate_final_score(s):
    score = 0
    consecutive_heads = 0
    
    for result in s:
        if result == 'H':
            score += 2
            consecutive_heads += 1
            if consecutive_heads == 3:
                break
        elif result == 'T':
            score -= 1
            consecutive_heads = 0
    
    return score


s =str(input("enter the string: "))
print(calculate_final_score(s)) 


# In[8]:


def nearest_corner(S, A):
    # Find index of S in A
    idx = A.index(S)
    
    # Determine left and right neighbors
    left_neighbor = A[idx - 1] if idx > 0 else None
    right_neighbor = A[idx + 1] if idx < len(A) - 1 else None
    
    # Check if S is adjacent to a gap ("-")
    if left_neighbor == '-' or right_neighbor == '-':
        return 0
    else:
        # Calculate minimum distance to the nearest corner seat
        min_distance = float('inf')
        
        # Calculate distance to the left corner gap
        if left_neighbor == '-':
            min_distance = idx
        
        # Calculate distance to the right corner gap
        if right_neighbor == '-':
            min_distance = min(min_distance, len(A) - 1 - idx)
        
        return min_distance

# Example usage:
S = "3C"
A = ["1A", "2B", "-", "3C", "4D"]

result = nearest_corner(S, A)
print(result)  # Output: 0


# In[5]:


def toss(string):
    score=0
    count=0
    for s in string:
        if s=='H':
            score+=2
            count+=1
            if count==3:
                break
        elif s =='T':
            score-=1
            count=0
    return score
string=str(input("enter the string: "))
print(toss(string))    


# ### 
# 19) Nearest Corner
# Bruce is a newly hired employee at a company. The Office Management Department
# has given him a desk number, which is stored in string S. He has also been handed a
# string array A. containing all the N office desk numbers.
# Array A also includes the symbol"-", which stands for the gap in the sitting
# arrangement. Comer seats are those that are on either side of the gap. Your task is to
# help Bruce find and retum an integer value. representing how far he is from the
# nearest corner seat. Return 0, if he is in the corner seat.
# Note:
# There will always be at least one gap in the string array A
# Desk number is always in a format of a number first followed by an English letter in
# uppercase
# Assume 0 - based indexing
# Input Specification:
# A string S. representing Bruce's newly assigned desk number.
# Second line containing space seperated strings showing the seat positions and gaps
# Sample input:
# 3C
# 1A 2B - 3C 4D
# Sample Output:
# 0
# '''

# In[1]:


input=input()
input2=input().split()
x=input2.index(input1)
z=float()
for i in range(x+1,len(input2)):
    if(input2[i]=="-"):
        


# '''
# 30) Boring Arrays
# You are given an array A of size N. In one operation you can select any two elements
# from it, add their absolute difference in your score.
# Your task is to find and return an integer value, representing the maximum score.
# Note:
# Assume 1 based indexing
# The elements on which operation has been performed cannot be selected again.
# Input Specification:
# Input1: An integer value N, representing the size of array A
# input2: An integer array A
# Output Specification:
# Return an integer value, representing the maximum score
# Sample Input:
# 4
# 1 2 3 4
# Sample Output:
# 4
# '''### 

# In[14]:


def max_score(N, A):
    
    
    
    max_score = 0
    for i in range(1, N):
        max_score += A[i] - A[i-1]
    
    return max_score

N = 4
A = [1, 2, 3, 4]
print(max_score(N, A)) 


# In[2]:


n=int(input())
a=list(map(int,input().split()))
    
start=0
end=-1
res=[]
while(len(a)>1):
    res.append(abs(a[start]-a[end]))
    a.pop(start) #pop-delete
    a.pop(end)
print(sum(res))        


# ### salt and pepper
# Problem Statement:
# In a quaint village nestled between rolling hills, there were N different salt containers
# and N different pepper containers in two separate groups. Each container had a
# specific level of bitterness, represented by arrays A and B respectively. The task at
# hand was to form N combinations, each consisting of one salt container and one
# pepper container
# However, there was a twist to the challenge. The objective was to arrange the
# combinations in such a way that the maximum bitterness level, which is the sum of
# salt and pepper quantities in each combination, was minimized.
# Print the lowest possible maximum bitterness level.
# Input Format:
# The first line contains a single integer N, the number of salt and pepper containers in
# each group.
# The second line contains N space-separated integers, denoting the bitterness level of
# N salt containers.
# The third line contains N space-separated integers, denoting the bitterness level of N 
# Sample Innput:
# 3
# 1 3 5
# 2 8 6
# Sample Output:
# 11
# 

# In[1]:


def solver(n,salt,pepper):
    #salt=0
   #pepper=0
    r=[]
    for i in range(len(salt)):
        r.append(salt[i]+pepper[i])
    return max(r)   
n=int(input())
salt=list(map(int,input().split()))
pepper=list(map(int,input().split()))
res = solver(n,salt,pepper)
print(res)


# ### Arduino
#  
# Tom is an Arduino Programmer. He has designed a program to run his robocar on a
# horizontal number line. Initially, the car is parked at: 0.
# Given an array A of N integers which can be A. B. C... the robocar runs as follows as
# per the designed program
# First the robocar moves A units in specified direction(right in case the integer is
# positive and left if the integer is negative).
# Then robocar first moves A units and then B units in a specified direction.
# In the next step, the robocar moves A units. B units, and then C units in a specified
# direction.
# This process keeps on repeating as per the number of integers in the sequence..
# Your task is to find and retum an integer value, representing the farthest coordinate
# reached by the robocar from the beginning to the end of the process.
# Sample Input:
# 1 -2 3 4
# Sample Output:
# 6
# '''

# In[3]:


n=list(map(int,input().split()))
print(sum(n))


# ### 21) Pizza Party
# Angela has decided to throw a pizza party. she has ordered N number of pizzas to be
# served to her N number of friends. In this way, she will be serving only one pizza to
# each friend.
# She now wants to invite fewer people to her party in order to provide more pizzas per
# person. But at the same time, she wants to ensure that there are at least Y friends at
# her party.
# Your task is to help Angela find and return an integer value, representing the sum of
# digits of the minimum number of friends that she can invite to the party, ensuring
# that each person gets an equal number of pizzas
# Sample Input:
# 100 17
# Sample Output:2

# In[3]:


def pizzaproblem(N,friends):
    for i in range(friends,N+1):
        if(N%i==0):
            return sum(map(int,str(i)))
N=int(input())
friends=int(input())
print(pizzaproblem(N,friends))


# ### vowel count

# In[32]:


def Vowel_count(str):
    count=0
    vowel=set("AEIOUaeiou")
    for letter in str:
        if letter in vowel:
            count=count+1
    print("no of vowels:",count)
str="Happy fathers day"
vowel_count(str) 




# In[7]:


def Vowel_count(str):
    
    first=0
    lst=['a','e','i','o','u']
    for i in str:
        if(i in lst):
            first=i
            break

    for i in str:
        if(i==first):
            return i
str=input()
print(Vowel_count(str))        


# ### encoding(IMPORTANT)
# You work in the message encoding department of a national security agency. Every message
# that is sent from or received in your office is encoded. you have a string containing , alpha numeric characters.
# of N is squared and the squares are concatenated together to encode the original number.
# Your task is to find and return an integer value representing the encoded value of the
# number.
# input1: An a string  representing the number and chracters 
# Output :
# Return an integer value representing the encoded value of the number
# input format:
# "hello 123 good morning"
# output:
# 149

# In[19]:


def encode(str):
    ls=[]
    for i in str:
        if(i.isdigit()):
            ls.append(i)
    return ls        
            
        
str=input()
print(encode(str))


# ###  pyramid sum
# 
# 
# 

# In[23]:


def pyramid_sum(pyramid):
    # Start from the second last row and move upwards
    for i in range(len(pyramid) - 2, -1, -1):
        # Iterate through each element in the current row
        for j in range(len(pyramid[i])):
            # Calculate the sum of the current element and the two elements below it
            pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])

    # The result is now stored at the top of the pyramid
    return pyramid[0][0]

# Example usage:
pyramid = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

result = pyramid_sum(pyramid)
print("The maximum path sum in the pyramid is:", result)


# In[2]:


n=int(input())
result=n*1
num=2
for i in range(n-1,0,-1):
    result+=2*i*num
    num+=1
print(result)


#  

# In[1]:


def reduce_till_zero(X, Y):
    while Y != 0:
        if X <= Y:
            return X
        else:
            T = X - Y
            X = Y
            Y = T
    return X


X = 48
Y = 18
result = reduce_till_zero(X, Y)
print(result)  


# ### '''
# Equilibrium
# You are given an array A of N integers. An equilibrium position is a position where the
# sum of all integers on its left is equal to the sum of all integers on its right in the array
# A. Print the index of the equilibrium position.
# Note:For any given array there is only a single equilibrium position, if no equilibrium
# position is found then print "NOT FOUND" without quotes.
# The array is 1 indexed.
# Input Format:
# The input consists of two lines:
# The first line contains an integer denoting N.
# The second line contains N space-separated integers denoting the elements of the
# array A.
# Input will be read from the STDIN by the candidate
# Output Format:
# Print the index of the equilibrium position. If no index is found, print "NOT FOUND"
# Sample Input
# 5
# 2 4 3 2 7
# Sample Output
# 3
# '''

# In[2]:


def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        if left_sum == total_sum - left_sum - arr[i]:
            return i + 1  # Return 1-indexed position
        
        left_sum += arr[i]
    
    return "NOT FOUND"

# Example usage:
arr = [2, 4, 3, 2, 7]
result = find_equilibrium_index(arr)
print(result)  # Output: 3


# In[ ]:



def gcd(a,b):
    while(b>0):
        
        temp=a
        a=b
        b=temp%b
    return a
def lcm(a,b):
    return((a*b)//gcd(a,b))
a=int(input("enter the num1"))
b=int(input("enter the num2"))
print(gcd(a,b))
print(lcm(a,b))



