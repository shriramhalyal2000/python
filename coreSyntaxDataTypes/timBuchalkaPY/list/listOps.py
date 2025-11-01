# list is a collection of multiple values

lists=["apple", "banana", "jackFruit" ,"grapes", "mangoes"]
# print(lists)
#
# for i in lists:
#     print(i)

for i, item in enumerate(lists):
    print(f"Item {item} is at index {i}")

if "apple" in lists:
    for i , item in enumerate(lists):
        if item=="apple":
            print(f"{item}, {i}")

print("*"*100)
for index, item in enumerate(lists):
    if item=="mangoes":
        print(f"{item}, {i}")
print("*"*100)
print(lists)
print("*"*100)
print("*"*100)
print(lists[:-1])# prints list with end value less
print("*"*100)
print(lists[::-1])# reverse the lists
print("*"*100)
print(lists[4::-2])# skips every second in revers order skips even number index
print("*"*100)
print(lists[3::-1])