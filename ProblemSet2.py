# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 06:07:29 2021

@author: QAQ
"""

#%%      
def problem2_1():
    lis=list(range(20,30))
    print(lis[3])
    print(lis)
    for i in range(20,30):
        print(i+1,end=' ' )
      


#%%

#%%  

alist = ["a","e","i","o","u","y"]
blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"] 

def problem2_2(my_list):   
    print(my_list)
    print(my_list[0])
    print(my_list[-1])
    print(my_list[3:5])
    print(my_list[:3])
    print(my_list[3:])
    print(len(my_list))
    my_list.append('z')
    print(my_list)
    



#%%


#%%
newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]
def problem2_3(ne):
   for i in ne:
       print(i, "has", len(i), "letters.")

    
#%%


#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    lis=[]
    num=0
    while num<10:
        lis.append(random.random()*5+30)
        num=num+1
    print(lis)
    
    
#%%

import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    random.seed(171)  # don't remove when you submit for grading
    for i in range(0,10):
        print(random.randint(1,6))
        
        

#%%
#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    for i in range(0,100):
        print(random.randint(1,6)+ random.randint(1,6) )

   
#%%
#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a=float(input("Enter length of side one:"))
    b=float(input("Enter length of side two:"))
    c=float(input("Enter length of side three:"))
    s = 0.5*(a + b + c)
    area= (s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of a triangle with sides",a,b,c,"is",area)
    
#%%


#%%
hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]
    
#%%
def problem2_8(temp_list):
    sum_of_temps = 0
    max_temp = None
    min_temp = None
    for hourly_temp in temp_list:
        sum_of_temps += hourly_temp
        if max_temp is None or max_temp < hourly_temp:
            max_temp = hourly_temp
        if min_temp is None or min_temp > hourly_temp:
            min_temp = hourly_temp
    ave_temp = sum_of_temps / len(temp_list)
    print("Average:", ave_temp)
    print("High:", max_temp)
    print("Low:", min_temp)

    
#%%