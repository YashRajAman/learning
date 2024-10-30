#!/bin/python3

import math
from operator import index
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps1(arr):
    
    sorted_arr = [x for x in range(1, len(arr)+1)]
    
    i=0
    j=len(arr)-1
    
    swaps = 0
    
    while (i<j):
        
        if arr == sorted_arr:
            return swaps
        
        if arr[i] == sorted_arr[i]:
            i += 1
            continue

        current_value = arr[i]
        actual_value = sorted_arr[i]
        actual_index = arr.index(actual_value)
        arr[i] = actual_value
        arr[actual_index] = current_value
        print("i: >>", (i, actual_index), (current_value, actual_value), arr)
        swaps += 1
        i += 1
        
        if arr[j] == sorted_arr[j]:
            j -= 1
            continue


        current_value = arr[j]
        actual_value = sorted_arr[j]
        actual_index = arr.index(actual_value)
        arr[j] = actual_value
        arr[actual_index] = current_value
        print("j: >>", (j, actual_index), (current_value, actual_value), arr)
        swaps += 1
        j -= 1
        
    return swaps
            
            


def minimumSwaps(arr):
    
    sorted_arr = [x for x in range(1, len(arr)+1)]
    indexed_dict = {i:arr[i] for i in range(len(arr))}
    rindexed_dict = {arr[i]:i for i in range(len(arr))}

    # print(arr)
    # print(sorted_arr)
    # print(indexed_dict)
    # print(rindexed_dict)

    i=0
    j=len(arr)-1
    
    swaps = 0
    
    while (i<j):
        print("===============")
        if indexed_dict[i] == sorted_arr[i]:
            i += 1
            continue
        
        current_value = indexed_dict[i]
        actual_value = sorted_arr[i]
        actual_index = rindexed_dict[actual_value]
        indexed_dict[i] = actual_value
        indexed_dict[actual_index] = current_value
        swaps += 1
        
        if indexed_dict[j] == sorted_arr[j]:
            j -= 1
            continue
        
        
        print(indexed_dict)
    return swaps
            
    

if __name__ == '__main__':
    arr = [[1,2,3,4], [4, 3, 1, 2], [2, 3, 4, 1, 5], [1, 3, 5, 2, 4, 6, 7]]
    results = [0, 3,3,3]

    for i in range(len(results)):
        res = minimumSwaps(arr[i])
        if res == results[i]:
            print("Pass")
        else:
            print("Fail")
    

