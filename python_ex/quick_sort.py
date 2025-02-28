def partition(ar, low, high):
    pivot = ar[high]
    i=low -1
    for j in range(low, high):
        if ar[j]<= pivot:
            i += 1
            ar[i], ar[j] = ar[j], ar[i]
            
    ar[i+1], ar[high] = ar[high], ar[i+1]
    return i+1




def quicksort(ar, low=0, high=None):
    if high == None:
        high = len(ar) - 1
    
    if low < high:
        pivot_index = partition(ar, low, high)
        quicksort(ar, low, pivot_index-1)
        quicksort(ar, pivot_index+1, high)
        




my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)