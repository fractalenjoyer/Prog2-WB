def gcd(*arr):
    while arr[0]!=arr[1]:
        arr = sorted(arr)
        arr = [arr[0], arr[1]-arr[0]]
    return arr

print(gcd(175,98))