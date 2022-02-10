def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(int(n / 10))


N = int(input("Enter the number: "))
result = sum_of_digit(N)
print("Sum of digits is", result)

