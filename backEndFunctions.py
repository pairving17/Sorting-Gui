#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:29:21 2019

@author: pairving17students.desu.edu
"""
from SortingFuncs import *



#class Node:
#    def __init__(self, dataval=None):
#        self.dataval = dataval
#        self.nextval = None
#        
#
#class SLinkedList(element,node):
#    def __init__(self):
#        self.headval = None
#    
#
#    def listprint(self):
#        printval = self.headval
#        while printval is not None:
#            print (printval.dataval)
#            printval = printval.nextval
#    def append(v):
#        global intlist
#        intlist += v
#
#intlist = SLinkedList()
#ninelinkedList = intlist

theDict = {             #item % 10
       0:[],
       1:[],
       2:[],
       3:[],
       4:[],
       5:[],
       6:[],
       7:[],
       8:[],
       9:[]
       
       }

def append(v):
    """
    this func appends new items to key values 
    without collusion by using chaining with lists
    v is item
    key is v % 10
    
    """
    
    global theDict
    l = []
    l = theDict.get(v % 10) # init list l to dic.get("21") 
    l += [v]            # adds 101 11 21 to the end of list l
    theDict.update({v%10:l})   # updates dict dic
#    print(theDict,"\n")
    

def convertStr(vari):
    """
    this is to be used for be saved into theList 
    vari is the var for str entryBar.get() 
    this func returns  aconvert entry.get() and return an int list 
    """  
    #create str list 
    splitstrlist = [ ]
    intlist = []
    splitstrlist = vari.split(" ")
    
    
    #convert str list to int list 
    for i in range(len(splitstrlist)):
        intlist.append(int(splitstrlist[i]))
    
    #return intlist
    
    return intlist

