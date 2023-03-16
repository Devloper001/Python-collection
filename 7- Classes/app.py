# // CLASSES //
# Class: blueprint for creating new objects
# Object: Instance of a Class

# Class: Human
# Objects: John, Mary, Jack


# // CREATING A CLASS //
class Point:
    # first letter of every word should be uppercase
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
