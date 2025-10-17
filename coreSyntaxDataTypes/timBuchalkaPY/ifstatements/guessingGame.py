# guessing game using simle if else and elif conditional statements

answer=5
guess=int(input("please enter your guess between 1 and 10:\n"))

if guess > answer:
  print("your guess is higher, please guess lower value.")
elif guess < answer:
  print("your guess is lower, please guess higher.")
else:
  print("you have guessed thr right answer!!!")