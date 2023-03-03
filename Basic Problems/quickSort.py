class Solution:
    def partition(self,arr,low,high):
        pivot = low
        i = low
        j = high
        while (i<j):
            while (arr[i]<= arr[pivot] and i < high):
                i += 1
            
            while (arr[j] > arr[pivot] and j > low):
                j -= 1
            
            if (i<j):
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j
        
    def quickSort(self,arr,low,high):
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSort(arr, low, pIndex-1)
            self.quickSort(arr, pIndex+1, high)
    