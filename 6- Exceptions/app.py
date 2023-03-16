# // EXCEPTIONS //
# a error called exception:
numbers = [1, 2]
print(numbers[3])
# a exception of type value error: (given we give input a character instead of integer)
age = int(input("Age: "))


# // HANDLING  EXCEPTIONS //
try:
    age = int(input("Age: "))
except ValueError:
    print("you didnt enter a valid age.")
print("execution continues")
# to combine different errors and return only one statement for cleaner code
try:
    age = int(input("Age: "))
except (ValueError, ZeroDivisionError):
    print("you didnt enter a valid age.")


# // CLEANING UP //
file = open("app.py")
# try, except, else
# finally:
# file.close()


# // RAISING EXCEPTIONS //
# to raise exception by ourselfs
def calulate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calulate_xfactor(-1)
except ValueError as error:
    print(error)


# raising exceptions cost 4x time so raise it when you really need it and it make it difficult when you scale your program.
