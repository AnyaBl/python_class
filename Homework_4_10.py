
A1 = [1, 5, 3, 5, 6, 8, ]
B1 = [2, 3, 9, 0, 11, 12]
C = sorted(set(A1) - set(B1))
print("Manual result : ", list(C))
# need to sort manually using sorted , turn into set to do subtraction

C2 = []
for item in A1:
  if item not in B1:
    C2.append(item)
print("Difference via the loop", C2) # result with duplicates, sorted

C3= list(set(A1).difference(set(B1)))
print("Result via the function: ", sorted(C3))
     #  need to sort , turn into set