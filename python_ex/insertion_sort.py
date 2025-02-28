my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)


for i in range(1, n):
    curr = my_array[i]
    j = i-1
    while(j >= 0 and my_array[j] > curr):
        my_array[j+1] = my_array[j]
        j -= 1
        
    my_array[j+1] = curr
    
print(my_array)    
        
        