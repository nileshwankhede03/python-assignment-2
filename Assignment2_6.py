
def Display(number):
    for i in range(number):
        for j in range(number-i):
            print(" * ",end="")
        print()

def main():
    number = int(input("Enter the row & colmn value "))
    Display(number)

if __name__ == "__main__":
    main()