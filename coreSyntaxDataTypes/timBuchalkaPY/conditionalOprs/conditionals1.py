# conditional operators

answer=5



# if guess!=answer:
#   if guess > answer:
#     print("Guess lower")
#   elif guess < answer:
#     print("Guess higher")
#   else:
#     print("You've guess accurately")
# else:
#   print("You've guess accurately")
guess=int(input("please enter your guess between 1-10:\n"))
if guess != answer:
  print("You've guessed inaccurately!!")
  guess=int(input("Plese try again now:\n"))
  if guess > answer:
    print("You've guessed inaccurately, try guess lower!")
  elif guess < answer:
    print("You've guessed inaccurately, try guessing higher")
  else:
    print("Hurray!!, you've guessed accurately")
else:
  print("Hurray!!, you've guessed accurately")