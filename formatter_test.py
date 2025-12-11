import math
import os


def add_numbers(a, b):
    result = a + b
    return result


def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2


def main():
    print("Sum :", add_numbers(2, 3))
    print("Area:", calculate_circle_area(5))
    print("cwd:", os.getcwd())
    print("test")


if __name__ == "__main__":
    main()
