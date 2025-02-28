def binary_search(ar, tar, s, n):
    
    while s<=n and tar >= ar[s] and tar<= ar[n]:
        
        mid = s + ((n - s) // (arr[n] - arr[s])) * (target - arr[s])
        print(mid)
        if ar[mid] == tar:
            return mid
        elif ar[mid] > tar:
            n = mid-1
        elif ar[mid] < tar:
            s = mid+1
    
    
# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
if result != -1:
    print(f"Binary Search: Element found at index {result}")
else:
    print("Binary Search: Element not found")