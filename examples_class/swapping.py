if __name__ == '__main__':
    def swapList(newList):
        size = len(newList)

        # Swapping
        temp = newList[0]
        newList[0] = newList[size - 1]
        newList[size - 1] = temp

        return newList
