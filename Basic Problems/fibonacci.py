class Solution:
    def printFibb(self,n):
        fib = [1,1]
        for i in range(2,n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[:n]
