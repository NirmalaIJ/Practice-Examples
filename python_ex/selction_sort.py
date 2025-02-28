""" How it works:

Go through the array to find the lowest value.
Move the lowest value to the front of the unsorted part of the array.
Go through the array again as many times as there are values in the array. """


my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n):
    min_x = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_x]:
            min_x = j
        my_array[i], my_array[min_x] =  my_array[min_x], my_array[i]
            
            
print(my_array)            