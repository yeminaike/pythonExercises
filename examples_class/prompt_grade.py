def prompt_grade():
    Counter = 0
    while Counter != 3:
        grade = int(input('Enter grade score of the student: '))

        if 90 <= grade <= 100:
            print("The student had an excellent grade A1")

        elif 70 <= grade <= 89:
            print("The student had a B very good.")

        elif 50 <= grade <= 69:
            print("The student had an average grade is C")

        elif 40 <= grade <= 49:
            print("The student had a poor grade")

        elif 30 <= grade <= 39:
            print("The student had a very poor grade")

        elif 0 <= grade <= 30:
            print("The student has a zero talent")
        else:
            print("invalid number")
            Counter += 1


if __name__ == '__main__':
    prompt_grade()
