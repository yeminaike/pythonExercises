
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

            if __name__ == '__main__':
                Assignment.equilateral_traingle()