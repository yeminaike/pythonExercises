

def palindrome():
    number = int(input("Enter a number: "))
    temp = number
    reverse_num = 0

    while number > 0:
     digit = number % 10
    reverse_num = reverse_num * 10 +digit
    number = number // 10

    if temp == reverse_num:
     print("Given the palindrome")
    else:
        print("Given number is not palindrome")

if __name__ == '__main__':
    palindrome()