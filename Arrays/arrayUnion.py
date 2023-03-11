class Solution:
    def mergeArrays(self,a,b,n,m):
        i = 0
        j = 0
        last_added = None
        union = []
        while i < n and j < m:
            if a[i] < b[j]:
                if a[i] != last_added:
                    union.append(a[i])
                    last_added = a[i]
                i += 1
                
            elif a[i] > b[j]:
                if b[j] != last_added:
                    union.append(b[j])
                    last_added = b[j]
                j += 1
            else:
                if a[i] != last_added:
                    union.append(a[i])
                    last_added = a[i]
                i += 1
                j += 1
        while i < n:
            if a[i] != last_added:
                union.append(a[i])
                last_added = a[i]
            i += 1
        while j < m:
            if b[j] != last_added:
                union.append(b[j])
                last_added = b[j]
            j += 1
        return union