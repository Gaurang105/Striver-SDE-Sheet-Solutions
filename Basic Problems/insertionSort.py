class Solution:
    def insertionSort(self, alist, n):
        for i in range(0,n,+1):
            j=i
            while (j>0 and alist[j-1] > alist[j]):
                temp = alist[j-1]
                alist[j-1] = alist[j]
                alist[j] = temp
                j = j-1
        return alist