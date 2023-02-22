class Solution:
    def divisorSum(N):
        sum = 0
        for i in range(1,N+1):
            sum += int(N/i)*i
        return int(sum)