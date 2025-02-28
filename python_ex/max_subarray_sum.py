""" maximum subarray sum


total sub arrays   (n(n+1))/2

Maximum Subarray Sum – Kadane’s Algorithm
 """
""" 
ar = [2,  3, 4, 4, -1, 3, -10, 7]


ans = ar[0]
temp_sum = 0
for i in ar:
    temp_sum += i
    ans = max(ans, temp_sum)
    if temp_sum < 0:
        temp_sum = 0
    print(ans)
     """
    
    
    
""" #not complete#
#rain water trapping
def trap(self, A):
        arr = list(A)
        res = 0
        for  i in range(1, len(arr)-1):
        
            lmax = arr[i]
            for j in range(i):
                
                lmax = max(lmax, arr[j])
                
            rmax = arr[i]
            for j in range(i+1, len(arr)):
                rmax = max(rmax, arr[j])
                
            res += (min(lmax, rmax) - arr[i])
        return res

""" 
#rotate matrix by 90
# https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/

ar= [[1 ,2],
        [3, 4]]

'''#becomes

a= [31
    42] '''

for i in range(len(ar)):
    for j in range(0, i):
        ar[i][j], ar[j][i] = ar[j][i], ar[i][j]
print(ar)
#then reverse  fr 90 rotation

for i in ar:
    i.reverse()
print(ar)
