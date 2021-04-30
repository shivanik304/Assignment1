# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:28:06 2021

@author: IT LAB
"""
1
import random

target=random.randint(1,20)

print('Target is between 1 and 20.')
for numbertaken in range(1,7):
    print('Enter your target.')
    yourtarget=int(input())
    if yourtarget<target:
        print('Target achieved is too low')
    elif yourtarget>target:
        print('Target achieved is too high.')
    else:
        break
        
if yourtarget==target:
   print('good job! You have achieved your target in'+ str(numbertaken) +'attempts!')
else:
    print('nope. the target was'+str(target))
 
        
      