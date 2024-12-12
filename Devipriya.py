#!/usr/bin/env python
# coding: utf-8

# In[6]:


L1=[] 
L2=[] 
n1=int(input("Enter the Numbers of list for L1: "))
n2=int(input("Enter the Numbers of list for L2: "))
for i in range(n1): 
    n3=int(input("Enter a number: ")) 
    L1.append(n3) 
    print(L1)
a=sum(L1)
print(f"Sum of the L1 list elements= {a}")

for j in range(n2): 
    n4=int(input("Enter a number: ")) 
    L2.append(n4) 
    print(L2)
b=sum(L2)
print(f"Sum of the L2 list elements= {b}")

if(a==b):
    print("Both lists elements have same sum")
else:
    print("Both lists elements sum are not same")
    
    
print(f"L1 sum is {a} \nL2 sum is {b}")
print(f"{a}!={b}")


# In[10]:


L1=[] 
L2=[] 
n1=int(input("Enter the Numbers of list for L1: "))
n2=int(input("Enter the Numbers of list for L2: "))
for i in range(n1): 
    n3=int(input("Enter a number: ")) 
    L1.append(n3) 
    print(L1)
for j in range(n2): 
    n4=int(input("Enter a number: ")) 
    L2.append(n4) 
    print(L2)
if(n1==n2):
    print("L1 and L2 have same element ")
else:
    print("L1 and L2 does not have same element ")


# In[3]:


def math(x,y,z):
    sum=x+y+z
    product=x*y*z
    return(f"sum={sum}, product={product}")
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
print(math(x,y,z))


# In[9]:


def leapy():
    p=int(input("Current year:"))
    q=int(input("Final year:"))
    for i in range(p,q):
        if(i%4==0 or i%100!=0 and i%400==0):
            print(i)
leapy()


# In[15]:


L=[]
n=int(input("Enter the range of the list"))
for i in range(n):
    a=int(input("Enter a number: ")) 
    L.append(a) 
    print("Integers:",L)
L1=[i for i in L if i>0]
print("Positive integers from the above list",L1)


# In[32]:


N=int(input("Enter a number"))
L1=[i*i for i in range (N)]
print(L1)


# In[36]:


word="albhIbet"
vowels=['a','i','e','o','u']
present=[i for i in word.lower() if i in vowels]
print(present)


# In[3]:


word="albhabet"
value=[ord(char) for char in word]
print("Given value is",word)
print("Orginal values are :",value)


# In[36]:


Name=['anju','achu','sree','maahi']
counter=0
for i in Name:
    for j in i:
        if j=='a':
            counter+=1
print("The occurence of 'a' in the list of names is",counter ,"times")


# In[28]:


Names=['anju','achu','sree','maahi']
counter=sum(i.lower().count('a')for i in Names)
print(counter)


# In[3]:


word='onion'
split=word.split()
for i in split:
    if(i==split):
        print(i)


# In[ ]:





# In[ ]:




