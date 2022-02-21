import random
import math

def make_list(filename):
    with open(f"{filename}.txt", "w") as file:
        list_one = []
        for element in range(1000):
            random_list = random.sample(range(100), 10)
            random_string = " ".join(map(str, random_list)) + '\n'
            list_one.append(random_string)
        file.writelines(list_one)



        assert len(list_one) != 0  # перевірка що список не нульовий
        assert len(list_one) == 1000  # перевірка що список має 1000 рядків
        assert random_string.count(" ") == 9 # перевірка що кількість пробілів 9 ( якщо 9 пробілів то 10 елементів в рядку)
        assert type(list_one) is list
        assert type(random_string) is str

make_list("text1.txt")


def list_to_power(filename):
    with open(f"{filename}.txt", "r+") as file:
        list_new = file.readlines()
        for line in list_new:
            result = [int(element) ** 2 for element in line.split()]
            file.write(" ".join(map(str, result)) + '\n')

        assert type(list_new) is list
        assert len(list_new) == 1000  # перевірка що список має 1000 рядків
        assert len(result) == 10  # перевірка що кількість елементів в рядку - 10
        assert len(list_new) != 0
        assert type(result) is list


list_to_power("text1.txt")
