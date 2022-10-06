

if __name__ == '__main__':
    eggs = int(input("Enter the number of eggs: "))
    boxes = int(eggs /6)
    uncompleted = eggs % 6

    if uncompleted <= 5:
        boxes += 1

        needed = 6 - uncompleted

        print(f" The completed egg boxes is {boxes}\n"
              f" The number of eggs in the uncompleted box is {uncompleted}\n The number of eggs"
              f" needed to fill up the last box is {needed}")