import math

if __name__ == '__main__':
    user_input = int(input("Enter a number: "))
    total_sum =0

    for counter in range(1, user_input):
        if user_input % counter == 0:
            total_sum = total_sum + counter

,         if total_sum == user_input:
            print("This is a perfect number :")

        else:
            print("zero Talent")




