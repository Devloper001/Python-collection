# // CONTROL TYPES //


# // CONDITIONAL STATEMENTS
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("Its Nice")
else:
    print("Its cold")
# this statement prints regardless of conditions
print("Done")


# // TERNARY OPERATOR //
#  Cleaner way to write conditional statements
age = 18
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


# //  LOGICAL OEPRATORS //
# and, or, not


#  // SHORT CIRCUIT EVALUATION //
# stoppage of execution of boolean operation if the truth value of expression has been determined already.


# // CHAINING COMPARISION OPERATORS //
if age >= 18 and age < 65:
    print("eligible")


# // QUIZZ //
# determine output of this:
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")


# solution:
# number and string are not equal hence no printing
# bag > apple but bag != cat hence no printing
# c will get printed


# // FOR LOOPS //
for x in range(2, 30, 3):
    print(x)
# ranges from (2,30) and increment the sequence with 3


# // NESTED LOOPS //
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


#  // ITERABLE //
for x in [1, 2, 3, 4]:
    print(x)


# // WHILE LOOPS //
number = 100
while number > 0:
    print(number)
    number //= 2


# // INFINITE LOOPS //
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == quit:
        break
