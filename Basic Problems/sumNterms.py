class Solution:
    def sumOfSeries(self,N):
        sum = 0
        for i in range(1,N+1):
            sum += i*i*i
        return sum