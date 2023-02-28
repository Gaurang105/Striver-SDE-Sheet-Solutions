class Solution:
    def selectionSort(self, arr,n):
        for i in range(n-1):
            mini = i
            for j in range(i+1, n):
                if arr[j] < arr[mini]:
                    mini = j
            temp = arr[mini]
            arr[mini] = arr[i]
            arr[i] = temp
        return arr