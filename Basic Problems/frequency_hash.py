class Solution:
    def frequencySolution(self, arr, N, P):
        hash = {}
        for i in arr:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        count = 1
        for i in range(N):
            if count<=P and count in hash:
                arr[i] = hash[count]
                count += 1
            else:
                arr[i] = 0
                count += 1
                