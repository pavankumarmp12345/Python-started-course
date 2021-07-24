# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 02:52:44 2021

@author: QAQ
"""


#%%
def problem3_1(txtfilename):
    infile=open(txtfilename)
    cc=0
    for row in infile.read():
        cc=cc+len(row)
        print(row, end="")
    print("\n\nThere are", cc, "letters in the file.")
    infile.close()
    

#%%
nlis = [23,64,23,46,12,24]          # list
atup = ("c","e","a","d","b")        # tuple
str1 = "Rumplestilskin"             # string


#%%

def problem3_2(collection):
   for i in collection:
       print(str(i))
#%%




#%%
def problem3_3(month, day, year):
    month_text = ("January","February","March","April","May","June","July","August","September","October","November","December")
    print(month_text[month-1]," ",  day,", ", year, sep="")
#%%


#%%
def problem3_4(mon, day, year):
    month_number = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, \
                    "September": 9, "October": 10, "November": 11, "December": 12}
    print(month_number[mon],"/",  day,"/", year, sep="")
#%%

#%%

def problem3_5(name):
    phone_numbers = {"abbie":"(860) 123-4535", "beverly":"(901) 454-3241", \
                      "james": "(212) 567-8149", "thomas": "(795) 342-9145"}
    print(phone_numbers[name])
    

#%%




# %%
import csv

def problem3_7(csv_pricefile, flower):
    ifh = open(csv_pricefile,newline='')
    data = {}
    for line in csv.reader(ifh):
        data[line[0]] = line[1]
    print(data[flower])

# %%
