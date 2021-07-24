# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 05:21:36 2021

@author: QAQ
"""

#%%

def problem4_1(wordlist):
    """ Takes a word list prints it, sorts it, and prints the sorted list """
    print(wordlist)
    wordlist.sort(key=str.lower)
    print(wordlist)
    
#%%


#%%
import random
numList = []
random.seed(150)
for i in range(0,25):
    numList.append(round(100*random.random(),1))
#%%   
def problem4_2(ran_list):
    """ Compute the mean and standard deviation of a list of floats """        
    import statistics
    print(statistics.mean(ran_list))
    print(statistics.stdev(ran_list))
    
#%%

#%%
def problem4_3(product, cost):
    """ Prints the product name in a space of 25 characters, left-justified
        and the price in a space of 6 characters, right-justified"""
    print('{0:<25}'.format(product) + '$' +'{0:>6.2f}'.format(cost))


#%% 

