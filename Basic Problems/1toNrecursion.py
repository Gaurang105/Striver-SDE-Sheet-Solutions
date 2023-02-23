class Solution:
    def printNos(self, N):
        if(N<1):
            return 0
        elif (N>0):
            print(N, end=" ")
            self.printNos(N-1)