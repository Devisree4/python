#!/usr/bin/env python
# coding: utf-8

# In[1]:


Name=input("Enter :")
first=Name[0]
result=first+Name[1:].replace(first,'$')
print(result)


# In[5]:


Name=input("enter:")
name1=Name[-1]+Name[1:-1]+Name[0]
print(name1)


# In[13]:


s="hello.java"
st=s.split('.')
print(st[0])


# In[12]:


for i in range(20,0,-2):
    print(i)


# In[6]:


for i in range(20):
    if(i%2==0):
        a=20-i
        print(a)
    


# In[15]:


a=input("enter a number:")
for i in a:
    print(i)
for j in i(i,0,-i):
    print(j)


# In[30]:


def word_count(str):
    counts=dict()
    words=str.split()
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(word_count("hello hai how are you hello"))
        


# In[8]:


Colorlist=input("Enter the colors:")
List=Colorlist.split(',')
print(f"First Color:{List[0]}")
print(f"Last Color:{List[-1]}")


# In[7]:


color_list1=input("Enter the colors:")
list1=color_list1.split(',')
color_list2=input("Enter the colors:")
list2=color_list2.split(',')
result=[i for i in list1 if i not in list2]
print(result)
    


# In[17]:


word=input("Enter the word:")
word1=word.split(' ')
print(word1[-1]+word1[0])


# In[1]:


word=input("Enter first String:")
word1=input("Enter Second String:")
str1=word1[0]+word[1:]
str2=word[0]+word1[1:]
result=str1+ " " + str2
print("After swapping:" + result)


# In[21]:


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0: 
            factors.append(i)
    return factors

for num in range(start, end + 1):
    factors = find_factors(num)
    print(f"Factors of {num}: {factors}")


# In[35]:


d={}
n=int(input("How many:"))
for i in range(n):
    key=int(input("Enter your id:"))
    value=input("Enter your name:")
    d[key]=value
    
d1=sorted(d.items())
d1=dict(d1)
print("Ascending order: ",d1)
d2=sorted(d.items(),reverse=True)
d2=dict(d2)
print("Descending order: ",d2)


# In[23]:


dict1={}
dict2={}
n1=int(input("how many:"))
for i in range(n1):
    key=int(input("Enter your id:"))
    value=input("Enter your name:")
    dict1[key]=value
print(dict1)
n2=int(input("how many:"))
for i in range(n2):
    key=int(input("Enter your id:"))
    value=input("Enter your name:")
    dict2[key]=value
print(dict2)
dict1.update(dict2)
print(dict1)


# In[3]:


a=1
n=int(input("Enter a number:"))
for i in range(1,n+1):
    a*=i
print(f"{n}!={a}")


# In[ ]:


def fibonacci_series(N):
    fib_series = []
    a, b = 0, 1
    for _ in range(N):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
N = int(input("Enter the number of terms: "))
result = fibonacci_series(N)
print("Fibonacci series:", result)


# In[17]:


N = int(input("Enter the number of terms: "))
a=0
b=1
fib=[]
for i in range(N):
    fib.append(a)
    c=a+b
    a=b
    b=c
print("Fibonacci series:",fib)


# In[49]:


L1=[]
b=0
n=int(input("Enter the no of terms:"))
for i in range(n):
    a=int(input("Enter the number:"))
    L1.append(a)
    print(L1)
for j in L1:
    b+=j
print("Sum of list:",b)


# In[50]:


n=[647,348,864]

for i in n:
    i=str(i)
    f=0
    for j in i:
        if int(j)%2!=0:
            f=1
    if f==0:
        print(i)


# In[33]:


import math

def even(number):
    for digit in str(number):
        if int(digit) % 2 != 0: 
            return False
    return True

def squares(start, end):
    results = []
    for num in range(start, end + 1):
        if even(num):
            sqrt = math.isqrt(num)
            if sqrt * sqrt == num:
                results.append(num)
    return results

perfect_squares = squares(start, end)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if perfect_squares:
    print(f"Perfect squares with all even digits in the range {start} to {end}:")
    print(perfect_squares)


# In[13]:


string = input("Enter a string:") 
count = 0
for char in string:
    count += 1
print(f"The number of characters in the string is: {count}")


# In[7]:


string = input("Enter a string: ")
if(string[-3:])=='ing':
    result=string+"ly"
else:
    result=string+"ing"
print("After checking:",result)


# In[12]:


wrd = input("Enter a list of words :")
words=wrd.split()
longest = 0

for word in words:
    if len(word) > longest:
        longest = len(word)

print(f"The length of the longest word is: {longest}")


# In[15]:


area_square = lambda side: side ** 2
area_rectangle = lambda length, breadth: length * breadth
area_triangle = lambda base, height:(1/2)*base * height

side = 4
length = 5
breadth = 3
base = 6
height = 2

print(f"Area of square with side {side}: {area_square(side)}")
print(f"Area of rectangle with length {length} and width {breadth}: {area_rectangle(length, breadth)}")
print(f"Area of triangle with base {base} and height {height}: {area_triangle(base, height)}")


# In[11]:


N=int(input("Enter the number:"))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()


# In[14]:


n = 4
for i in range(1, n+1):
    print("* " * i)

for i in range(n-1, 0, -1):
    print("* " * i)


# In[ ]:




