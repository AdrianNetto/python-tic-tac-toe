def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def user_choice():
    while True:
        choice = input("Please enter a number (0-8): ")

        if not choice.isdigit():
            print("This is not a digit!")
            continue
            
        choice = int(choice)

        if choice not in range(0, 9):
            print("Sorry, you are out of the acceptable range (0-8)")
            continue
            
        return choice

display(row1, row2, row3)

user_choice()