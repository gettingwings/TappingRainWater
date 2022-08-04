
from copy import deepcopy
import numpy as np


def capacity(levels, result):

    print(levels, end='\n\n')

    # making a 2D array with zeros
    arr = np.zeros((max(levels), len(levels)));
    
    # to fill 2D array with values
    # row by row
    for r in range(0,max(levels)):
        # populate row r
        arr[r, :] = levels
        proxy_level = []

        # calculate values for r+1 in the same loop
        for i in levels:
            x = i-1  # next row will have values reduced by 1
            if x == -1:  # all the -1 will be changed to 0
                proxy_level.append(0)
            else:
                proxy_level.append(x)
        levels = deepcopy(proxy_level)
 
    water = 0  # water at each level
    total_water = 0  # total water
    numbers_left = 0  # numbers >0 for each row will be stored
    flag = False  # will be used to ignore the starting nums if they are same
   
    for r in range(0,arr.shape[0]):
        # counting all the number more than 0
        for num in arr[r,:]:
            if(num>0):
                numbers_left += 1
        # print( f'numbersLeft {numbers_left}' )
        
        # if numbers>1 left are more than 1 only then filling will be possible  
        # as that will create a cavity 1.......1    
        if numbers_left>1:
            cc = 0  # to tackle last same numbers
            if arr[r,0]>0:
                cc += 1
            for c in range(1, arr.shape[1]-1):
                if arr[r,c]>0:
                    cc += 1    
                if cc >= numbersLeft:
                    break
                              
                if arr[r, c-1] == arr[r, c] and flag == False:
                    pass
                elif arr[r, c-1] >= arr[r, c] and arr[r, c] <= arr[r, c+1] and arr[r, c] == 0:
                    flag = True
                    water += 1
                    arr[r,c] = 200
                          
        flag = False        
        print(arr[r, :], water, sep=" :::  ")
        total_water += water
        water = 0
        numbersLeft = 0
        
    print(f'\nResult should be..{result}........Total water calculated is..{total_water} \n\n')
        

capacity([1, 0, 1, 2, 3, 0, 1, 2], 4)

capacity([0, 1, 0, 1, 0, 1, 0, 2, 1], 3)
 
capacity([0, 0, 0, 1, 0, 2, 1, 0, 1, 2], 5)

capacity([2, 0, 1, 4, 3, 0, 2, 0, 3, 0, 4], 19)

capacity([0, 1, 0, 2, 1, 0, 0, 0, 1, 2], 9)

capacity([1, 1, 0, 2, 4, 0, 0, 0, 0, 2, 0, 0], 9)

capacity([2, 1, 0, 2, 4, 3, 4, 4, 0, 2, 0, 1], 7)

capacity([0, 1, 0, 2, 1, 0, 1, 0, 2], 7)

capacity([1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 0)

capacity([1, 1, 0, 0, 1, 1, 1, 0, 0, 0], 2)

capacity([1, 2, 0, 0, 1, 2, 1, 0, 0, 2], 10)

# GettingWings :)