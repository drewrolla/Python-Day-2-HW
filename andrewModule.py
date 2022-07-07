from math import pi

def squareFoot():
    l = int(input("What is the length of your house? "))
    w = int(input("What is the width of your house? "))
    return f"The square footage of your house is {int(l) * int(w)}"


# circumference = pi * diameter

def circle():
    d = int(input("What is the diameter of the circle? "))
    return pi * d


