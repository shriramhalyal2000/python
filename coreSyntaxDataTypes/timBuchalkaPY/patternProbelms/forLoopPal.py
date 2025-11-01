list=[1, 2, 3, 4, 3, 2 ,1]

is_palindrome=True

for i in range(len(list)//2):
    if list[i]!=list[-(i+1)]:
        is_palindrome=False
        break

if is_palindrome:
    print("given list is palindrome")
else:
    print("given list is not palindrome")