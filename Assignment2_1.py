from Arithmetic import *

def main():
    value1 = int(input("Enter first value : "))
    value2 = int(input("Enter second value : "))

    ret = 0

    ret = Add(value1,value2)
    print("Addition is : ",ret)

    ret = Sub(value1,value2)
    print("Substraction is : ",ret)


    ret = Mult(value1,value2)
    print("Multiplication is : ",ret)

    ret = Div(value1,value2)
    print("Division is : ",ret)

if __name__ == "__main__":
    main()