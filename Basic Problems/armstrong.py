class Solution:
    def armstrongNumber(ob, n):
        if (int(str(n)[0])**3 + int(str(n)[1])**3 + int(str(n)[2])**3)==n:
            return "Yes"
        else:
            return "No"
