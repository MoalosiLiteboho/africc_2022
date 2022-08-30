def main():
    while True:
        results = 0
        is_calulated = True
        first_number = float(input("Enter the first number: "))  # Accepting user-input as float
        operating_sign = input("Enter the operating sign: ")
        second_number = float(input("Enter the second number: "))  # Accepting user-input as float

        if operating_sign.__eq__("+"):
            results = first_number.__add__(second_number)
        elif operating_sign.__eq__("-"):
            results = first_number.__sub__(second_number)
        elif operating_sign.__eq__("*"):
            results = first_number.__mul__(second_number)
        elif operating_sign.__eq__("**") or operating_sign.__eq__("^"):
            results = first_number.__pow__(second_number)
        elif operating_sign.__eq__("/"):
            if second_number.__eq__(0):
                print("The result is ZERO as you can't divide by 0")
                is_calulated = False
            else:
                results = first_number.__divmod__(second_number)
        else:
            print("Invalid operating sign entered!!! \nTRY AGAIN !!!")

        if is_calulated:
            print("Results : " + str(results))

        choice = input(
            "Do you want to try to use calculator again (yes / no): ")  # Accept user-input whether user want to run code again

        if choice.lower().startswith("y"):  # Check user input whether it start with y for yes, run code if it is
            continue  # Continue to loop the while loop
        break  # Break out of the while loop


if __name__ == '__main__':
    main()
