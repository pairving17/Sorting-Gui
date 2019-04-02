#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:49:51 2019

@author: pairving17students.desu.edu
"""

def F(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return F(n-1) + F(n-2)


print(F(4))