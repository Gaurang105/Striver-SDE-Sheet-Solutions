class Solution:
    def bubbleSort(self,arr, n):
        for i in range(n-1, 0, -1):
            for j in range(0,i,+1):
                if arr[j] > arr[j+1]:
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp
        return arr