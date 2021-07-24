# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 02:52:44 2021

@author: QAQ
"""



#%%
def problem1_1():
    print("Problem Set 1")

    
#%%



#%%
def problem1_2(x,y):
    print( x+y)
    print(x*y)

#%% 

#%%
def problem1_3(n):
    my_sum=0
    for num in range(n+1):
        my_sum=my_sum+num
    print(my_sum)

#%%

#%%
def problem1_4(miles):
   print("There are", 5280*miles,  "feet in", miles, "miles.")
    
#%%

#%%
def problem1_5(age):
    if age<7:
        print("Have a glass of milk.")
    elif 7<age<21:
        print("Have a coke.")
    else:
        print("Have a martini.")
   
    
#%%

#%%
def problem1_6():
   for i in range(1,100,2):
       print(i, end= " ")


    
#%% 



#%%
def problem1_7():
    b1_str=input ("Enter the length of one of the bases:")
    b1=float(b1_str)
    b2_str=input ("Enter the length of one of the bases:")
    b2=float(b2_str)  
    h_str=input("Enter the height:")
    h=float(h_str)
    print("The are of trapezoid with bases", b1, "and", b2, " and height", h, "is", (b1+b2)*h/2)
  
    
    
    
#%%
