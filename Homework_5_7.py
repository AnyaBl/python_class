def multiply(a, n):
    if n == 0:
        return (a[n])
    else:
        return (a[n] * multiply(a, n -1))


array = [1, 3, 3, 4, 5, 6, 8]
n = len(array)

print(multiply(array, n - 1))
