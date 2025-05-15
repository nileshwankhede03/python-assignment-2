
def CountDigits(number):
    sum = 0

    while(number != 0):
        iDigit = number % 10
        sum = sum + iDigit
        number = number // 10

    return sum


def main():
    number = int(input("Enter the number to count digits : "))
    iRet = CountDigits(number)

    print("Number of digits are : ",iRet)

if __name__ == "__main__":
    main()