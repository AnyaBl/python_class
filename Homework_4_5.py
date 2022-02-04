
set_1 = {"a",  "d", "o", "k"}
set_2 = {"c", "d", "e","k" }

result =set_1.isdisjoint(set_2)
result_duplicates = set_1.intersection(set_2)

if result is True:
    print("No duplicates found")
else:
    print("Duplicates: ", result_duplicates)
