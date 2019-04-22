# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:18:29 2019

@author: Jonas Lindemann
"""

from math import sqrt

print(__name__)

def is_prime(n):

    prime = True
    
    k = 2
    while k<=sqrt(n) and prime:
        if (n % k == 0):
            prime = False
            break
        k+=1      

    return prime      