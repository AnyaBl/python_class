
tuple1= (1, 2, 3, 4)
tuple2= (3, 5, 2, 1)
tuple3= (2, 2, 3, 1)


list1 = list(tuple1)
list2 = list(tuple2)
list3 = list(tuple3)

list4 = (list1[0]+list2[0]+list3[0], list1[1]+list2[1]+list3[1], list1[2]+list2[2]+list3[2], list1[3]+list2[3]+list3[3])
tuple_final = tuple(list4)
print("The sum tuple is:", tuple_final)
