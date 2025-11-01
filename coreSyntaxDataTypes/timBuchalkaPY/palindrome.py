pal=[1, 3, 4, 56, 9]
drome=[1234, 2345, 1234]
if pal==pal[::-1]:
    print(f"given list{pal} is a palindrome")
else:
    print(f"given list {pal} is not a palindrome")

print(pal[::-1])

if drome==drome[::-1]:
    print(f"given list {drome} is palindrome")
else:
    print(f"given list {drome} is not a palindrome")