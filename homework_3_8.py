
first_list = [25, 28, 49, 31, 82, 90, 45, 88]
second_list = [56, 11, 45, 31, 91, 99, 88]

set_difference= set(first_list).symmetric_difference(set(second_list))
list_difference = list(set_difference)

print(list_difference)