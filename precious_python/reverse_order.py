

def reverse_number():
    number = int(input("Enter a number with multiple figure: "))

    while number > 0:
        figure = number % 10
        number = number // 10
        print(figure, end= " ")

if __name__ == '__main__':
    reverse_number()
