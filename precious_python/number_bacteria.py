class Assignment:

    @staticmethod
    def bacteria_start_with(bacteria):
        print(f'Hour\t\tNumber of bacteria')
        for hours in range(0, 20, 5):
            output = bacteria * 2 * hours
            print(f'{hours}\t\t\t{output}')

if __name__ == '__main__':
    Assignment.bacteria_start_with(200)