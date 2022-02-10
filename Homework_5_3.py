def func(*arguments):
    for t in arguments:
        print("Index:", arguments.index(t),", " "argument ", t)


print(func(5, 25, 31, 67, 104, 56, 78))