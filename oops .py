#!/usr/bin/env python
# coding: utf-8

# In[1]:


class INT :
    def __init__(self,nm,ag,gn):
        self.name = nm
        self.age = ag
        self.gender = gn


st1 = INT("sahana",20,'F')

print(st1.name,st1.age,st1.gender)

print(type(st1))


# In[2]:


class STD:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None

st2 = STD()

st2.name = input("Enter your Name: ")
st2.age = int(input("Enter your age: "))
st2.gender = input("Enter Your Gender: ")


print(st2.name,st2.age,st2.gender)


# In[3]:


class STUDENT :
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.gender = c

a = input("Enter your Name: ")
b = int(input("Enter your age: "))
c = input("Enter Your Gender: ")


st3 = STUDENT(a,b,c)

print(st3.name,st3.age,st3.gender)

st3.age =21

print(st3.name,st3.age,st3.gender)


# In[4]:


a =1
b ='sdfg'
c = 2.4
d = ['sdg','sd',1,3]
e = {1:"sdfg",2:"fsfdsf"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# In[5]:


st4 = INT("abc",21,'M')
print(st4.name,st4.age,st4.gender)
print(type(st4))


# In[6]:


#Inheritance

class A:
    def __init__(self,a,b):
        self.A = a
        self.__B = b
        
    def printB(self):
        print(self.__B)

ob1 = A(2,5)

print(ob1.A)
ob1.printB()


# In[7]:


#create A Student Class that Holds the deatils of Students like Name USN and the Marks in 5 subjects percentage and grade.
#create 5 studnet object and get the data for name usn and marks after that find the percentage and grade and store it to the class object.

class Std:
    def __init__(self): 
        self.__USN = None
        self.__Name = None
        self.__Marks = []
        self.__Percentage = None
        self.__Grade = None

    def Std_Input(self):
        self.__Name = input("Enter your Name: ")
        self.__USN = input("Enter Your USN: ")
        for i in range (0,5):
            marks = input(f"Enter Your Marks in Sub{i+1} : ")
            self.__Marks.append(marks)

    def calc_percentage (self):
        sum = 0
        for i in self.__Marks:
            sum = sum + int(i)
        self.__Percentage = (sum/500)*100

    def calc_Grade(self):
        per = float(self.__Percentage)
        if per<=100 and per >=80:
            self.__Grade = "A"
        elif per<80 and per >=60:
            self.__Grade = "B"
        elif per<60 and per >=40:
            self.__Grade = "C"
        elif per<40 and per >=0:
            self.__Grade = "D"
        else: 
            self.__Grade = "Inavlid"

    def print_details(self):
        print("Name: ",self.__Name)
        print("USN : ",self.__USN)
        print("Marks in Five Subject are :")
        for i in range(0,5):
            print(f"Subject {i+1} = {self.__Marks[i]}")
        print("Percentage : ", self.__Percentage)
        print("Grade : ", self.__Grade)



st1 = Std()

print(type(st1))


# In[10]:


st1.Std_Input()


# In[11]:


st1.print_details()


# In[12]:


st1.calc_percentage()
st1.print_details()


# In[13]:


st1.calc_Grade()
st1.print_details()


# In[ ]:




