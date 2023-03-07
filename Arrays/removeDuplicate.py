class Solution:	
	def remove_duplicate(self, A, N):
	    if N==0:
	        return 0
	    count = 1
	    for i in range(1,N):
	        if A[i]!=A[i-1]:
	            A[count] = A[i]
	            count += 1
	    return count