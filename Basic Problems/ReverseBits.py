class Solution:
    def reversedBits(self, X):
        binary = bin(X)[2:]
        binary = binary.zfill(32)

        reversed_binary = binary[::-1]
        reversed_int = int(reversed_binary, 2)

        return reversed_int