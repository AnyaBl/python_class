def isPower2(n):
    if (n & (n-1))==0:
        return "Yes"
    else:
        return "No"

print(isPower2(128))
print(isPower2(4))
print(isPower2(32))
print(isPower2(64))
print(isPower2(71))
print(isPower2(3))
print(isPower2(9))
