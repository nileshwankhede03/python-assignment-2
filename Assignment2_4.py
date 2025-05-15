
def AddtionOfFactors(number):
    sum = 0
    for i in range(1,int((number/2)+1)):
        if(number % i == 0):
            sum = sum + i
    return sum

def main():
    number = int(input("Enter number to find factorial "))
    ret  = AddtionOfFactors(number)

    print("Addtion Of Factors is : ",ret)


if __name__ == "__main__":
    main()