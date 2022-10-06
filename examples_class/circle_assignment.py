import math

if __name__ == '__main__':
    diameter = int(input("Enter the diameter: "))
    feet = int(input("Enter the feet: "))
    radius = diameter / 2
    square_feet = (radius * radius) * math.pi
    square_feet_per_acre = square_feet / 43560
    total_gallons = square_feet_per_acre * feet * 325851
    print("The  total gallon is: ", total_gallons)