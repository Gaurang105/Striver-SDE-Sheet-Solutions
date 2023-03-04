def largest( arr, n):
    large = arr[0]
    for i in range(n):
        if arr[i] > large:
             large = arr[i]
    return large
            