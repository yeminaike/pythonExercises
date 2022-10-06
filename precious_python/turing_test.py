class Assignment:



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


if __name__ == '__main__':
    Assignment.turing_test()
