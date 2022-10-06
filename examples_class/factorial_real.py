import math

if __name__ == '__main__':
    number = int(input('Enter a number: '))
    sum = 0
    for counter in range(1,number):
        if number % counter == 0:
            sum += counter
            print(counter)
    print('The sum is ', sum)
    if sum == number:
        print('This is a perfect number!')
    else:
        print('Zero number')





