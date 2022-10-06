# Calculate the area and circumference of a circle from its radius.
# Step1: Prompt for a radius.
# step2: Apply the area formula.
# step3: print out of the results.


import math


if __name__ == '__main__':

    radius_str = input("Enter the radius of your circle: ")
    radius_int = int(radius_str)

    circumference = 2 * math.pi * radius_int
    area = math.pi * (radius_int ** 2)

    print("The circumference is:",circumference,", and the area is:",area)


