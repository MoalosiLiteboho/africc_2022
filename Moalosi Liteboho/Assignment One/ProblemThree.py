def main():
    while True:
        sentence = input("Enter the sentence of your choice \nSentence > ")  # Accepting user-input and store it
        words = sentence.split()
        words.sort()

        for word in words:
            print(word)

        choice = input("Do you want to try again? \nAnswer > ")  # Accept user-input whether user want to run code again

        if choice.lower().startswith("y"):  # Check user input whether it start with y for yes, run code if it is
            continue  # Loop the while loop again
        break  # break while loop if if-statement didn't get executed


if __name__ == '__main__':
    main()
