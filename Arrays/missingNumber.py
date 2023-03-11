# Solution-1
def missingNumber( A, N):
     A = sorted(A)
     for i in range(N-1):
         if A[i] != i+1:
             return i+1
     return N

# Solution-2

def missingNumber( A, N):
    actual_sum = N * (N+1)//2
    missing_num = actual_sum
    for i in range(N-1):
        missing_num -= A[i]
    return missing_num