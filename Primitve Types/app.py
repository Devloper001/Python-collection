# PRIMITIVE TYPES

# // VARIABLES //
import math
student_count = 100
rating = 4.99
is_published = True
name = "Dhrupad Pandya"
print(student_count)


# // STRINGS //
course = "Python Programming"


# // BUILT IN FUNCTIONS FOR STRING //
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])


# // ESCAPE SEQUENCES //
# ESCAPE CHARACTER : \
# HERE ESCAPE SEQUENCE IS : \"
# FOR NEW LINE : \n
course = "Python \" Programming"
print(course)


# // FORMATTED STRINGS //
first = "Dhrupad"
last = "Pandya"
full = f"{first}middle{last}"
print(full)


# //STRING METHODS //
courses = " Python programming "
print(courses.upper())
print(courses.lower())
print(courses.title())
print(courses.strip())
print(courses.rstrip())
print(courses.lstrip())
print(courses.find("pro"))
print(courses.replace("p", "j"))
print("pro" in courses)
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
