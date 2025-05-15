
def Factorial(number):
    Fact = 1

    if(number == 0):
        return 0
    
    for i in range(1,number + 1):
        Fact = Fact * i

    return Fact

def main():
    number = int(input("Enter number to find factorial "))
    ret  = Factorial(number)

    print("Factorial is : ",ret)


if __name__ == "__main__":
    main()