#Exercise 3
import numpy as np
my_arr=np.arange(10)
print(my_arr)
my_arr[4:7]=25
print(my_arr)
#add .copy() function
arr_slice=my_arr[4:7].copy()

# Change the first element of arr_slice to -1
arr_slice[0]=-1
print(arr_slice)
print(my_arr)

