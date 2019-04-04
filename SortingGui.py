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
from backEndFunctions import*

master = Tk()
global theList


master.geometry(  )
Label(master, text="Enter Data").grid(row=0,column=0)

entryBar = Entry(master)
entryBar.grid(row=1,column=0)
Button(master, text = "Enter",command = enter).grid(row = 1,column=1, sticky = W)

OPTIONS = [
"Selection Sort",
"Insertion Sort",
"Radix Sort",
"Shell Sort",
"Merge Sort",
"Bubble Sort"
] #etc

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

selectSortBar = OptionMenu(master, variable, *OPTIONS)
selectSortBar.grid(row=2,column = 0)

#lable for labelBar
Label(master, text="Sorted: ").grid(row=3,column=0)

#display the sorted values in theList
labelStr = StringVar()
labelBar = Label(master, textvariable=labelStr)  #display the sorted values in theList
labelBar.grid(row=4, column = 0)


theList = []


#TODO write description for this func
def enter():
    global theList
    global theDict
    theList = convertStr(entryBar.get())
    i = 0
    for i in range(len(theList)):
        append(theList[i])

#TODO write description for this func
def ok():
    
    global theList
    
    if variable.get() == OPTIONS[0]:
        
        print(theList)
        print("\n")
        print(SelectionSort(theList))
        labelStr.set(theList)
        
    if variable.get() == OPTIONS[1]:
       
        print(theList)
        print("\n")
        print(InsertionSort(theList))
        labelStr.set(theList)
        
    if variable.get() == OPTIONS[2]:
        
        print(theList)
        print("\n")
        print(RadixSort(theList,))
        labelStr.set(theList)

    if variable.get() == OPTIONS[3]:
        
        print(theList)
        print("\n")
        print(ShellSort(theList))  
        labelStr.set(theList)
        
    if variable.get() == OPTIONS[4]:
        print(variable.get()+"WORKING")
        print(theList)
        print("\n")
        print(BubbleSort(theList))  
        labelStr.set(theList)

    


button = Button(master, text="OK", command=ok)
button.grid(row=2,column =1)
master.geometry("500x500")
mainloop()
