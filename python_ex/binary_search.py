""" efficient searching algorithm suitable for sorted lists
divides the search interval in half until the target value is found.
Steps:
Start with the entire sorted list.
Compute the middle element of the list.
If the middle element is equal to the target value, return its index.
If the middle element is less than the target value, search in the right half of the list.
If the middle element is greater than the target value, search in the left half of the list.
Repeat steps 2-5 until the target value is found or the search interval is empty.

 """

def binary_search(ar, tar, s, n):
    
    while s<n:
        mid = (s+n)//2
        if ar[mid] == tar:
            return mid
        elif ar[mid] > tar:
            n = mid-1
        elif ar[mid] < tar:
            s = mid+1
    
    
    
    
def binary_search(arr, target, low, high):
    """
    Perform binary search recursively to find the target value in the given sorted list.

    Parameters:
        arr (list): The sorted list to be searched.
        target: The value to be searched for.
        low (int): The lower index of the search interval.
        high (int): The upper index of the search interval.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1
    
        

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
if result != -1:
    print(f"Binary Search: Element found at index {result}")
else:
    print("Binary Search: Element not found")