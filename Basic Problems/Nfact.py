class Solution:
    def factorialNumbers(self, N):
        ans =[]
        def sol_recur(fact,x):
            if fact > N:
                return
            else:
                ans.append(fact)
                sol_recur(fact*x, x+1)
        sol_recur(1,2)
        return ans
