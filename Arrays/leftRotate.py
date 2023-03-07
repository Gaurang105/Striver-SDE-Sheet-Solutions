# Brute Force Method

class Solution:
    def leftRotate(self, arr, k, n):
        k = k % n
        temp = [0]*k
        
        for i in range(k):
            temp[i] = arr[i]
        
        for i in range(n-k):
            arr[i] = arr[i+k]
            
        for i in range(n-k, n):
            arr[i] = temp[i-(n-k)]


# Optimal Solution

class Solution:
    def leftRotate(self, arr, k, n):
        k = k % n
        arr[:k] = reversed(arr[:k])
        arr[k:n] = reversed(arr[k:n])
        arr[:n] = reversed(arr[:n])