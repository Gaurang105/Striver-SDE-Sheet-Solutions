class Solution:
    def printNos(self, N):
        if (N < 1):
            return
        elif (N >= 1):
            print(N, end=" ")
            self.printNos(N-1)
            