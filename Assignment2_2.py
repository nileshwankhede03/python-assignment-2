
def Display(rows):
    for i in range(rows):
        for j in range(rows):
            print(" * ",end="") # end="" use for same line nd only print() for next row
        print()

        
def main():
    number = int(input("Enter number of rows & columns "))
    Display(number)


if __name__ == "__main__":
    main()