#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:33:26 2019

@author: pairving17students.desu.edu
"""
#from SortingGui import theList

def SelectionSort(numbers):
   for i in range(len(numbers)-1):
      
      # Find index of smallest remaining element
      index_smallest = i
      for j in range(i+1, len(numbers)):
         
         if numbers[j] < numbers[index_smallest]:
            index_smallest = j
      
      # Swap numbers[i] and numbers[index_smallest]
      temp = numbers[i]
      numbers[i] = numbers[index_smallest]
      numbers[index_smallest] = temp
   return numbers


def InsertionSort(numbers):
    
    for i in range(len(numbers)): 
        j = i
        while(j>0 and numbers[j] < numbers[j-1]):
            
            temp = numbers[j] 
            numbers[j] = numbers[j-1]
            numbers[j-1] = temp
            j -= 1
    return numbers


def ShellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap //= 2
    return arr

      
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# TODO fix sorting 
def QuickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        QuickSort(arr, low, pi-1) 
        QuickSort(arr, pi+1, high) 
        
  
# TODO Fix RADIX Sort 
def Bubblesort(A):
    # modified from http://www.geekviewpoint.com/python/sorting/bubblesort
    swaps = []
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
            if (A[k] < A[k - 1]):
                swaps.append([k, k - 1])
                tmp = A[k]
                A[k] = A[k - 1]
                A[k - 1] = tmp
    return A, swaps
     








#Testing Sorting Methods 
l = [1,31,43,95,78,65,23,11,2,67,91,8]
print(l)
print(RadixSort(l))   