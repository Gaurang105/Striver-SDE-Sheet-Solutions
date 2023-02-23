class Solution:
    def printGfg(self, N):
        if (N<1):
            return
        elif (N>=1):
            self.printGfg(N-1)
            print("GFG", end=" ")
        