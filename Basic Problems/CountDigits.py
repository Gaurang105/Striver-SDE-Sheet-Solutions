#Given a number N. Count the number of digits in N which evenly divides N.

class Solution:
    def evenlyDivides (self, N);
        count = 0
        digits = map(int, list(str(N)))
        for d in digits:
            if d != 0 and N % d == 0:
                count +=1
        return count