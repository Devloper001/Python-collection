# PRIMITIVE TYPES


import math

# // VARIABLES //
student_count = 100
rating = 4.99
is_published = True
name = "Dhrupad Pandya"
print(student_count)


# // STRINGS //
course = "Python Programming"


# // BUILT IN FUNCTIONS FOR STRING //
print(len(course))
# return letter of that position
print(course[0])
print(course[-1])
# return letters inbetween these postions
print(course[0:3])
# return letter from beginning of string
print(course[:3])


# // ESCAPE SEQUENCES //
# Escape Character  : \
# Here Escape Sequence is : \"
# For New Line : \n
course = "Python \" Programming"
print(course)


# // FORMATTED STRINGS //
first = "Dhrupad"
last = "Pandya"
# a function which joins the strings together
full = f"{first}middle{last}"
print(full)


# //STRING METHODS //
courses = " Python programming "
# in uppercase
print(courses.upper())
# in lowercase
print(courses.lower())
# capitalize first letter of title
print(courses.title())
# leading and trailing whitespaces gets removed
print(courses.strip())
# trailing whitespaces are removed
print(courses.rstrip())
# leading whitespaces are removed
print(courses.lstrip())
# for searching particular string
print(courses.find("pro"))
# for replacing particular string
print(courses.replace("p", "j"))
# return true or false
print("pro" in courses)
# return true or false
print("swift" in courses)


# // NUMBERS //
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
# floor division (rounding off ans.)
print(10 // 3)
# Modulus
print(10 % 3)
# exponential
print(10 ** 3)

# // AUGUMENTED ASSIGNED OPERATOR //
x = 10
x = x + 3
x += 3


# // WORKING WITH NUMBERS //
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))
# google python3 math modules


# // Type Conversion
x = input("x: ")
y = x + 1
