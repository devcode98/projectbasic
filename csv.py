#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:21:21 2018

@author: devang
"""
import csv
import sys
import math
import numpy as np
import matplotlib.pyplot as py
list1=[]
with open('makemytrip_com-travel_sample.csv','r') as csvfile:
    



      y=csv.reader(csvfile,delimiter=',',quotechar= '"')
      for row in y:
        list1.append(row)  
        print (row)
        
print(type(list1))
list_cities=[]
i=0
while i< len (list1):
    list_cities.append(list1[i][1])
    i=i+1
vac=list1[0][2]
list_cities.append(vac)
# will be leaving the 'city' keyword 
i=1
while i<len(list1)    :
          if vac in list_cities:
              
              vac=list1[i][1]
              i=i+1
              
          else:
              vac=list1[i][1]
              list_cities.append(vac)
              i=i+1
i=0
emptylist=[]
var=list_cities[1]
emptylist.append(var)


while i<len(list_cities):              
      if var in  emptylist:
           var=list_cities[i]
           i=i+1
           
      else: 
          
          emptylist.append(var)
          var=list_cities[i]
          i=i+1
# now empty list contains all the seggregrated cities##
length_cities=len(emptylist)
print(length_cities)          
            
first=(emptylist[0])
n=1
while n<len(list1):
     if list1[n][6]== ' ':
         list1[n][6]=0
     if list1[n][6]=='1 star':
         list1[n][6]=1
     if list1[n][6]=='2 star':
         list1[n][6]=2
     if list1[n][6]=='3 star':
         list1[n][6]=3
     if list1[n][6]=='4 star':
         list1[n][6]=4
     if list1[n][6]=='5 star':
         list1[n][6]=5
     if list1[n][28]=='':
         list1[n][28]=0
     if list1[n][6]=='Four star':
         list1[n][6]=4
     if list1[n][6]=='Three on 5':
         list1[n][6]=3
     if list1[n][6]=='Four on 5':
         list1[n][6]=4
     if list1[n][6]=='Five on 5':
         list1[n][6]=5
     if list1[n][28]=='no':
         list1[n][28]=0
     n=n+1
n=1
listx=[]
listy=[]
i=1

while n<len(list1):
      list1[n][6]=float(list1[n][6])
      list1[n][28]=float(list1[n][28])
      n=n+1      
while i<len(list1):
      listx.append(list1[i][6])
      listy.append(list1[i][28])
      i=i+1
list_hotels=[]
i=1
counter=0
product=0
j=1
while i<len(list1):
    
    j=1
    while j<len(list1):
     if(str(list1[j][1]) == str(first)):
         counter=counter+1
     if str(first)=='city':
       j=j+1
     j=j+1
    list_hotels.append(counter)  
    counter=0
    i=i+1
    if i==757:
        break
    first=emptylist[i]
    if str(first)=='city':
       i=i+1

        
    
emptylist.pop(1)
emptylist.sort()
list_hotels.sort()
py.plot(emptylist[0:700],list_hotels[0:700],color='r')
i=0
j=0

    

