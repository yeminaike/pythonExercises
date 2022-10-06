
class Assignment:

    @staticmethod
    def hourly_wage(good, bad, principal):
        good_new_hourly_wage = principal * ((1 + 0.03) ** good)
        print(f'After {good} years of good reviews, new hourly wage is ${good_new_hourly_wage : .2f}')
        bad_new_hourly_wage = principal * ((1 - 0.03) ** bad)
        print(f' After {bad} years of bad reviews, new hourly wage is $s{bad_new_hourly_wage: .2f}')

if __name__ == '__main__':
   Assignment.hourly_wage(5, 2, 10)

