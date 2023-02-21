#Solution Type-1

class Solution:
    def lcmAndGcd(self, A , B):
        arr=[0]*2
        
        g = math.gcd(A,B)
        l = (A*B) // g
        
        arr[0],arr[1] = l,g
        
        return arr
    

#Solution Type-2

def gcd(A,B):
    if A == 0:
        return B
    gcd(B % A, A)

def lcm(A,B):
    return (A*B) // gcd(A,B)