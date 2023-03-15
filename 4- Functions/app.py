# // FUNCTIONS //


# // DEFINING FUNCTIONS //
def greet():
    print("Hi There")
    print("Welcome aboard")


greet()


#  // ARGUMENTS //
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Dhrupad", "Pandya")
# here 'first_name' and 'last_name' are parameters and
# 'Dhrupad' and 'Pandya' are Arguments


# // TYPES OF FUNCTIONS //
# 1- Perform a Task
# 2- Return a Value


# // KEYWORD ARGUMENTS  //
def increment(number, by):
    return number + by


print(increment(2, by=1))
# very easy to understand for user


# // DEFAULT ARGUMENTS //
def increment(number, by=1):
    return number + by


print(increment(2))
# here dafault value of by(1) will be used and if we provide another value thorugh argument that value would be used


# // XARGS //
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
# (2, 3, 4, 5) is a tuple
#  we cannot modify this collection(tuple) unlike lists but these are iterable


# // XXARGS //
def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)
# this creates dictionary data structures


# // SCOPE //
# A variable is only available from inside the region it is created. This is called scope.
message = "a"


def greet(name):
    global message
    message = "b"


greet("Mosh")
print(message)
# this is bad pratice global variables could be used by other functions which in result in undesired answers


# // VS CODE SHORTCUTS
# move any number of lines up/down - alt + up/down
# duplicate line(s) - alt + shift + up/down
