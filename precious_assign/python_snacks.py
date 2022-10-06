class Assignment:

    @staticmethod
    def equilateral_triangle():
        side_lengths = [0, 0, 0]
        for side in range(0, 3):
            length = int(input('Enter the length of the sides of a triangle: '))
        side_lengths[side] = length
        if side_lengths[0] == side_lengths[1] and side_lengths[1] == side_lengths[2]:
            print('The triangle is an equilateral triangle')
        else:
            print('The triangle is not equilateral')

    @staticmethod
    def fibonacci(position):
        total = 0
        count = 0
        number_before_1 = 0
        number_before_2 = 1
        if position == 1:
            print(f'The number in position {position} is 0')
        elif position == 2:
            print(f'The number in position {position} is 1')
        elif position >= 3:
            while count < position - 2:
                total = number_before_1 + number_before_2
                number_before_1 = number_before_2
                number_before_2 = total
                count += 1
        print(f'The number in position {position} is {total}')

    @staticmethod
    def grade_printing():
        grade = int(input('Enter name: '))
        if grade >= 90:
            print('congratulations!, your grade of ' + str(grade) + 'earns you an A in this course.')
        else:
            print('passed!')

    @staticmethod
    def heart_rate():
        age = int(input('Enter your age: '))
        maximum_heart_rate = 220 - age
        target_heart_rate = maximum_heart_rate / 2
        target_heart_rate_2 = 85 * maximum_heart_rate / 100
        print(f' Maximum heart rate: {maximum_heart_rate}bpm')
        print(f' Target heart rate is {target_heart_rate}bpm to {target_heart_rate_2}bpm.')

    @staticmethod
    def hourly_wage(good, bad, principal):
        good_new_hourly_wage = principal * ((1 + 0.03) ** good)
        print(f'After {good} years of good reviews, new hourly wage is ${good_new_hourly_wage : .2f}')
        bad_new_hourly_wage = principal * ((1 - 0.03) ** bad)
        print(f' After {bad} years of bad reviews, new hourly wage is $s{bad_new_hourly_wage: .2f}')

    @staticmethod
    def multiplication_table():
        for one in range(1, 11, 1):
            two = one * 2
            three = one * 3
            four = one * 4
            five = one * 5
            six = one * 6
            seven = one * 7
            eight = one * 8
            nine = one * 9
            ten = one * 10
            print(one, '', two, '', three, '', four, '', five, '', six, '', seven, '', eight, '', nine, '', ten,
                  '')

    @staticmethod
    def bacteria_start_with(bacteria):
        print(f'Hour\t\tNumber of bacteria')
        for hours in range(0, 20, 5):
            output = bacteria * 2 * hours
            print(f'{hours}\t\t\t{output}')

    @staticmethod
    def palindrome():
        number = int(input("Enter a number: "))
        temp = number
        reverse_num = 0

        while number > 0:
            digit = number % 10
        reverse_num = reverse_num * 10 + digit
        number = number // 10

        if temp == reverse_num:
            print("Given the palindrome")
        else:
            print("Given number is not palindrome")

    @staticmethod
    def reverse_number():
        number = int(input("Enter a number with multiple figure: "))

        while number > 0:
            figure = number % 10
            number = number // 10
            print(figure, end=" ")

    @staticmethod
    def turing_test():
        problem = input('What is your problem? ')
        history = input(f'Have you had this problem {problem} before? (yes or no)')
        if history == 'yes':
            print('Then you have this problem again.')
        elif history == 'no':
            print('Well, you have it now.')
        elif history != 'yes' and history != 'no':
            while history != 'yes' and history != 'no':
                if history == 'yes' or history == 'no':
                    break
                else:
                    print('Please, enter yes or no')
                    history = input('Have you had this problem before?')
                    if history == 'yes':
                        print('Then you have this problem again.')
                    elif history == 'no':
                        print('Well, you have it now.')

    @staticmethod
    def flu():
        total_cases = 0
        smallest_case = 9999999
        largest_case = 0
        for i in range(0, 7):
            cases = int(input('Enter the number of cases for the day: '))
            if cases < smallest_case:
                smallest_case = cases
            elif cases > largest_case:
                largest_case = cases
            total_cases += cases
            average_of_all_cases = total_cases / 7
            print(f'Total cases for week is {total_cases}')
            print(f'Average cases for week is {average_of_all_cases}')
            print(f'Smallest case is {smallest_case}')
            print(f'Largest case is {largest_case}')

    @staticmethod
    def eggs_per_box():
        eggs = int(input("Enter the number of eggs: "))
        boxes = int(eggs / 6)
        uncompleted = eggs % 6

        if uncompleted <= 5:
            boxes += 1

            needed = 6 - uncompleted

        print(f" The completed egg boxes is {boxes}\n"
              f" The number of eggs in the uncompleted box is {uncompleted}\n The number of eggs"
              f" needed to fill up the last box is {needed}")