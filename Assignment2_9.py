
def CountDigits(number):
    cnt = 0

    while(number != 0):
        cnt = cnt + 1
        number = number // 10

    return cnt


def main():
    number = int(input("Enter the number to count digits : "))
    iRet = CountDigits(number)

    print("Number of digits are : ",iRet)

if __name__ == "__main__":
    main()