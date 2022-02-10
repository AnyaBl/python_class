def outer():
    a = 1
    b = 2

    def inner():
        nonlocal a
        s = a + b
        print("Inner sum is :", s)
        a = a + 5

    inner()

    print("Sum with added 5: ", a + b)


outer()
