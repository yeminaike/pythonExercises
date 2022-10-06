class Assignment:

    @staticmethod
    def heart_rate():
        age = int(input('Enter your age: '))
        maximum_heart_rate = 220 - age
        target_heart_rate = maximum_heart_rate / 2
        target_heart_rate_2 = 85 * maximum_heart_rate / 100
        print(f' Maximum heart rate: {maximum_heart_rate}bpm')
        print(f' Target heart rate is {target_heart_rate}bpm to {target_heart_rate_2}bpm.')


if __name__ == '__main__':
    Assignment.heart_rate()
