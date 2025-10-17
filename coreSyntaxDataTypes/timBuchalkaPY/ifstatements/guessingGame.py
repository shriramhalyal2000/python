# guessing game using simle if else and elif conditional statements

answer=5
guess=int(input("please enter your guess between 1 and 10:\n"))

if guess > answer:
  print("your guess is higher, please guess lower value.")
  guess=int(input("Please try again:"))
  if guess==answer:
    print("You've guesed correctly")
  else:
    print("Better luck next time")
elif guess < answer:
  print("your guess is lower, please guess higher.")
  guess=int(input("enter your guess agaun:"))
  if guess==answer:
    print("You've finally got it")
  else:
    print("Better luck next time")
else:
  print("you have guessed thr right answer!!!")