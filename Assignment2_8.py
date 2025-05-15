
def Display(number):
    for i in range(number):
        for j in range(i + 1):
            print(j+1,end=" ")
        print()

def main():
    number = int(input("Enter the row & colmn value "))
    Display(number)

if __name__ == "__main__":
    main()