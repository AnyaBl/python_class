def list_sum(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total


print(list_sum(2, 2, 2, 777))
