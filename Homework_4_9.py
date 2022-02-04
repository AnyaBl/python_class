
A1 = [1, 5, 3, 5, 6, 8, ]
B1 = [2, 3, 9, 0, 11, 12]
C = sorted(A1+B1)
print("Manual result : ", (C))
# unifies with duplicates possible with lists also doesn't sort from the lowest number - need to use sorted function

C2 = set(A1)|set(B1)
print("Result with | operator ", list(C2))   # need to turn into set and then back , no duplicates, sorted

set(A1).union(B1)
print("Result via the function:", list(set(A1).union(B1)))
# need to convert list to set and then convert back to print but no duplicates and sorted

