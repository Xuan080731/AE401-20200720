# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:11:03 2020

@author: ASUS-UX21
"""

scores=[]
totel=0
highest=0
lowest=100

n=input("班上有幾位同學")
n=int(n)

for i in range(n):
    s=input('輸入成績')
    s=int(s)
    scores.append(s)
   
for j in range(n):
    if scores[j]>highest:
        highest=scores[j]
    if scores[j]<lowest:
        lowest=[scores]
print(scores)
print("總分是",totel)
print('平均分數是')        
print('最高分數是',highest)       
    

    
    
    
