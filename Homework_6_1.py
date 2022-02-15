def bubble_sort(t):
    # t = l.copy  # лишнє посилання і копіювання, можна зразу параметром поставити t в функцію bubble sort,  не потрібно копіювання
    for n in range(0, len(t)):
        for i in range(n):  # тут ітерувати i елемент потрібно по рейнджу n ,оскільки n приймає величину списка
            assert i in range(n)    # перевірка що і ітерується в рейнжі n
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]
    return t


nums = [4, 1, 6, 3, 2, 7, 8]
bubble_sort(nums)
print(nums)

assert type(nums) is list  # перевірка що введений nums є списком
assert len(nums) != 0   # перевірка що довжина списку не нуль
assert min(nums) == bubble_sort(nums)[0] # перевірка що в новому бабл списку перший елемент дійсно відповідає мінімальному елементу зі списку numm
assert len(nums) == len(bubble_sort(nums)) # перевірка що довжина двох списків (початкового і після бабл сортування однакова)