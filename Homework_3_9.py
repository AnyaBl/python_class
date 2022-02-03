
dictionary_1 = {1:10, 2:20}
dictionary_2 = {3:30, 4:40}
dictionary_3 = {5:50, 6:60}
dictionary_4 = {}
for item in (dictionary_1, dictionary_2, dictionary_3): dictionary_4.update(item)
print(dictionary_4)