#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:04:23 2019

@author: pairving17students.desu.edu
"""
#TODO: Link to a text file that holds the data
#TODO: INcorperate the difierent sorting methods 



from tkinter import *
from SortingFuncs import *


OPTIONS = [
"Selection Sort",
"Insertion Sort",
"Radix Sort",
"Shell Sort",
"Merge Sort"
] #etc

master = Tk()


my_list = [line.split(' ') for line in open("DataDoc.txt")]

theList= my_list[0]


variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

    

def ok():
    #print ("value is:" + variable.get()) 
    if variable.get() == OPTIONS[0]:
        print(variable.get()+"WORKING")
        print(theList)
        print("\n")
        print(SelectionSort(theList))
        
        
    if variable.get() == OPTIONS[1]:
        print(variable.get()+"WORKING")
        print(theList)
        print("\n")
        print(InsertionSort(theList))
        
        
    if variable.get() == OPTIONS[2]:
        print(variable.get()+"WORKING")
        print(theList)
        print("\n")
        print(RadixSort(theList,))
        
    if variable.get() == OPTIONS[3]:
        print(variable.get()+"WORKING")
        print(theList)
        print("\n")
        print(ShellSort(theList))  
    
    



button = Button(master, text="OK", command=ok)
button.pack()

mainloop()