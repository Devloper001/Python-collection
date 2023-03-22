import os
import datetime
import calendar
import random
from my_module import find_index, test
import sys
# only imports specific things

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print(sys.path)
# list of all direct ories available
# to import a module from different location:
# import sys, sys.path.append('/Users/dhrupadpandya/Desktop/My-Modules')

# generates random values
random_course = random.choice(courses)
print(random_course)


today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# print current Working Directory
print(os.getcwd())
# print location of file
# displays all attributes and method in module
print(os.__file__)
# prints all attributes and method defined in object
print(dir(find_index))


# the name of the module that starts our program is always main
