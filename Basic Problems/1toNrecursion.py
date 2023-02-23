class Solution:
    def printNos(self, N):
        if(N<1):
            return 0
        elif (N>0):
            self.printNos(N-1)
            print(N, end=" ")