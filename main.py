import pandas as pd
import os
def show_menu():
    print("\n===== Main Menu =====")
    print("1. Check the data")
    print("2. Show the data")

def check(data):
    if all(data['id'] > 0) and data['id'].is_unique and all(data['memory'] > 0) and all(data['arrival_time'] >= 0) and all(data['CPU_required'] > 0):
        return True
    else:
        return False

def show(data):
    print(data)


def main():
    file_name = input("Enter file name INCLUDING file extension: ") #user input line
    data = pd.read_csv(f'{file_name}', sep=' ', names=['id', 'memory', 'arrival_time', 'CPU_required', 'Quantum', 'ContextSwitch_Penalty'])
    #reads the file that the user provided and saves the columns with easy to remember and understand names

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            result  = check(data)
            print("Valid data!" if result else "Invalid data.")
        elif choice == 2:
            show(data)
        else:
            print("Invalid choice. Please try again.")

main()