import os


def main():
    while True:
        month = int(input("Enter the month in number: "))
        year = int(input("Enter the year: "))

        if 0 < month <= 12:
            print("\nDisplaying Month Calender: \n")
            month_calender = os.system("cal " + str(month) + " " + str(year))
            print(month_calender)

        choice = input("Do you want to use the program again? : \nChoice > ")  # Accepting user input

        if choice.lower().startswith("y"):  # Check user input whether it start with y for yes, run code if it is
            continue  # Loop again
        break  # Break while loop if if-statement didn't get executed


if __name__ == '__main__':
    main()
