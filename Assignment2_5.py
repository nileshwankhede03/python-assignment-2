
def ChkPrime(number):
    if(number <= 1):
        return False

    for i in range(2,number):
        if(number % i == 0):
            return False

    return True


def main():
    number = int(input("Enter the number "))
    ret  = ChkPrime(number)

    if(ret == True):
        print("Number is prime")
    else:
        print("Number is not Prime.")

if __name__ == "__main__":
    main()