class Assignment:

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


if __name__ == '__main__':
    Assignment.flu()


