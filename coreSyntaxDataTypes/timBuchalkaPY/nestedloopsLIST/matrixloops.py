matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
  for num in row:
    print(num, end=" ")#puts white space after the index value is printed in same row rathan than in vertical column
  print()#this print moves loop to next line after the num is iterated over in inner loop