class Solution:
	def print2largest(self,arr, n):
	    largest = arr[0]
	    Slargest = -1
	    for i in range(n):
	        if arr[i] > largest:
	            Slargest = largest
	            largest = arr[i]
	        elif (arr[i]< largest and arr[i] > Slargest):
	            Slargest = arr[i]
	           
	    return Slargest