#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[2]:


if 5 > 2:
  print("Five is greater than two!")


# In[3]:


if 5 > 2:
print("Five is greater than two!")
#indentation is more important otherwise it will display an error


# In[4]:


"""This is a
multiline docstring."""
print("Hello, World!") 
# a multi line docstring allows you to comment in multiple lines 


# In[6]:


x = "john"
y = "5"
print (x)
print (y)


# In[7]:


x = 5 
y = "sally"
print (x)
print (y)
# in python there is no need to declare the type of variable at all


# In[8]:


x = " awesome "
print (" python is " + x) 
# + is used to combine both text and a variable


# In[9]:


x = "Sir Iqbal"
y = " is a great trainer"
print ( x+y )
# you can also use a + sign to add two variables


# In[10]:


x = 5
y = 10 
print ( x + y )
# + sign acts as a mathematical operator in case of numbers 


# In[11]:


# there are three types of numbers in python 
x = 2 #int 
y = 2.5 #float
z = 2j #complex
print (x)
print (y)
print (z)


# In[12]:


# to verify the type of an object use can use the "type" parameter 
x = 3 #type int may be a positive or negative whole number of unlimited lenght 
y = 6.66 #type float includes a number with a floating point 
z = 34j #type complex includes a a character "j" as imaginary part
print (type(x))
print (type(y))
print (type(z))


# In[13]:


# How to print a part of a string 
x = "Hello World"
print (x[1]) #remeber that letter "H" has value "0"


# In[14]:


#strip removes the whitespaces at start and end 
x = "  Hello Pakistan    "
print (x.strip())
print (len(x)) #will return the lenght of that string including spaces
print (x.lower()) #will print the string in lower case
print (x.upper()) #will print the string in upper case
print (x.replace("H" , "J")) #Replace parameter will replace the selected Character
print (x.split("P")) #it will split the total string into two parts as shown in result.


# In[1]:


#Arithmetic Operators 

x = 5
y = 3

print(x + y)
#operator no 1 "+"


# In[2]:


x = 5
y = 3

print(x - y)
#operator no 2 "-"


# In[5]:


x = 5
y = 3

print(x * y)
#operator no 3 "*" 


# In[4]:


x = 12
y = 3

print(x / y)
#operator no 4 "/"


# In[6]:


x = 5
y = 2

print(x % y)
#Operator no 4 "%" it return what is left after dividing 5 and 2 
#Last Arithmetic Operator 


# In[7]:


#Assignment Operator 
x = 5

print(x)
# assign. operator no 1 it only assign the value 5 to vairable "x"


# In[8]:


x = 5

x += 3

print(x)
# assign. operator no 2 "+="   it acts same as x = x + 3


# In[9]:


x = 5

x -= 3

print(x)  
# assign operator no 3 "-=" it acts same as x = x - 3


# In[10]:


x = 5

x *= 3

print(x)
# assign. operator no 4 "*=" it acts same as x = x * 3 


# In[11]:


x = 5

x /= 3

print(x)
# assign. operator no 5 "/=" it acts same as x = x / 3


# In[12]:


x = 5

x%=3

print(x)
# assign. operator no 6 "%=" it acts same as x = x % 3


# In[13]:


x = 5

x//=3

print(x)
# assign. operator no 7 "//=" it acts same as x = x // 3 Floor Division 


# In[14]:


x = 5

x **= 3

print(x)
# assign. operator no 8 "**=" it acts same as x = x ** 3 Exponentiation 


# In[15]:


x = 5

x &= 3

print(x)
# assign. operator no 9 "&=" it acts same as x = x & 3 


# In[16]:


x = 5

x |= 3

print(x)
# assign. operator no 10 "|=" it acts same as x = x | 3 


# In[17]:


x = 5

x ^= 3

print(x)
# assign. operator no 11 "^=" it acts same as x = x ^ 3 


# In[18]:


x = 5

x >>= 3

print(x)
# assign. operator no 12 ">>=" it acts same as x = x >> 3 


# In[19]:


x = 5

x <<= 3

print(x)
# assign. operator no 13 "<<=" it acts same as x = x << 3


# In[20]:


#Comparison Operator of "equal to" 
x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3


# In[21]:


#Comparison Operator no 2 "Not equal to"
x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3


# In[22]:


#Comparison operator no 3 "Greator than"
x = 5
y = 3

print(x > y)

# returns True because 5 is greater than 3


# In[23]:


#Comparison operator no 4 "less than"
x = 5
y = 3

print(x < y)

# returns False because 5 is not less than 3


# In[24]:


#Comparison operator no 5 "Greator than, or equal to "
x = 5
y = 3

print(x >= y)

# returns True because five is greater, or equal, to 3


# In[25]:


#Comparison operator no 6 "Less than, or equal to"
x = 5
y = 3

print(x <= y)

# returns False because 5 is neither less than or equal to 3


# In[26]:


# Logical Operator no 1 "AND"
x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10


# In[27]:


#logical Operator no 2 "OR"
x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


# In[28]:


#logical Operator no 3 "NOT"
x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result


# In[29]:


#Identity Operator no 1 "IS"
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# In[30]:


#Identity operator no 2 "isnot"
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


# In[31]:


#Membership operator no 1 "in"
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


# In[33]:


#Membership operator no 2 "not in"
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


# In[ ]:




