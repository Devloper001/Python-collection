# // DATA STRUCTURES //

# // LISTS //
from collections import deque
letters = ["a", "b", "c"]
matrix = [[0, 1], [0, 2]]
# a list of 5 zeroes
zeros = [0] * 5
# to combine two lists
combined = zeros + letters
print(combined)
# a list of 0 to 20(20 is not included)
numbers = list(range(20))
print(numbers)
# to create a list of each character of string
chars = list("Hello World")
print(chars)
# to print length of list
print(len(chars))


# // ACCESSING ITEMS //
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0:3])
# return values at increment of 2 values
print(letters[::2])


# // LIST UNPACKING //
numbers = [1, 2, 3]
first, second, third = numbers

# to assign few var in big lists:
numbers = [1, 2, 3, 4, 4, 4, 4]
first, second, *other = numbers
print(first)
print(other)
# packing all others item in second list called other
# when we pass parameter with asterisk multiplied it stores all arguments passed to him
# for first and last items : first, *other, last


# // LOOPING OVER LISTS //
letters = ["a", "b", "c", "d"]
for index, letter in enumerate(letters):
    print(index, letter)
# enumerate function will return an enumerate object in each iteration it will return tuple of (index, letter)


# // ADDING OR REMOVING ITEMS //
letters = ["a", "b", "c"]
# Add
letters.append("d")
letters.insert(0, "-")
print(letters)
# Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
print(letters)


# // FINDING ITEMS //
letters = ["a", "b", "c"]
print(letters.count("d"))
if 'd' in letters:
    print(letters.index("d"))


# // SORTING LISTS //
# there there two methods:
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)
# for tuples:
# sort by price
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# // LAMBDA FUNCTIONS //
# cleaner way to sort tuples:
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort(key=lambda item: item[1])
print(items)


# // MAP FUNCTION //
# will insert all prices in new tuple prices
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)
# using map function:
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
print(prices)


# // FILTER FUNCTION //
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

x = filter(lambda item: item[1] >= 10, items)
print(x)


# // LIST COMPREHENSIONS //
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = [items[1] for item in items]
filtered = [item for item in items if item[1] >= 10]


# // ZIP FUNCTIONS //
list1 = [1, 2, 3]
list2 = [10, 20, 30]
# combines individual x and y of lists
print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2)))


# // STACK //
# LIFO
browsing_session = []
# to add item:
browsing_session.append(1)
# to remove item
browsing_session.pop()
# to add item to top of the stack
if not browsing_session:
    browsing_session[-1]


#  // QUEUES //
# FIFO
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")


# // TUPLES //
point = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")


# // SWAPPING VARIABLES //
# by using tuples:
x = 10
y = 11
x, y = y, x
print("x", x)
print("y", y)


# // ARRAYS //
numbers = array("i", [1, 2, 3])
