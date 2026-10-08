import pandas as pd
import os
def show_menu():
    print("\n===== Main Menu =====")
    print("1. Check the PCB")
    print("2. Show the PCB")
    print("3. Add to the PCB")
    print("4. Save as a new file")
    print("5. Run in FCFS")
    print("6. Run in SJF")
    print("7. Exit")
    #simple console line menu so that i dont need to make a gui

def check(data):
    if all(data['id'] > 0) and data['id'].is_unique and all(data['memory'] > 0) and all(data['arrival_time'] >= 0) and all(data['CPU_required'] > 0) and all(data['Quantum'] > 0) and all(data['ContextSwitch_Penalty'] > 0) and (data % 1 == 0).all().all():
        #this is a very long if statement that very simply makes sure that all of the values
        #in all of the columns of the dataframe are valid
        #also the final and makes sure that all values are integers
        return True

    else:
        return False

def show(data):
    print(data)
    #this function was very simple, im just printing the pandas database

def add(data):
    data.loc[len(data)] = [100, 3, 2, 1, 4, 5]

    #print(data) #commenting out this print function, but my proof of concept
    #is that now i have an empty row at the last row
    #so in order to add to it, the row number will be last row
    #print(data.iloc[-1, 0]) #YIPEE, THIS WORKS OKAY SO YOU ARE ABLE TO CALL EACH SQUARE OF THE ARRAY WTIH THIS SORT OF FUNCTION

    data.iloc[-1, 0] = int(input("Enter PCB ID: "))
    data.iloc[-1, 1] = int(input("Enter PCB Memory: "))
    data.iloc[-1, 2] = int(input("Enter PCB Arrival Time: "))
    data.iloc[-1, 3] = int(input("Enter PCB CPU Required: "))
    data.iloc[-1, 4] = int(input("Enter PCB Quantum: "))
    data.iloc[-1, 5] = int(input("Enter PCB ContextSwitch Penalty: ")) #amazing, these five lines work from
    #basic principles, im actually so happy i could code this

def runfcfs(data):
    #print(data)
    #print("poopsock")
    if data.empty:
        print("Sorry, you have no data")
        return

    count = 0

    TripTimes = []
    turnaround = []


    while not data.empty:
        #first we find the smallest arrival time required
        curr = data.loc[data['arrival_time'].idxmin()]
        TripTimes.append(curr['arrival_time'])

        #make sure it starts after the previous thing has ended
        start = max(count, curr['arrival_time'])
        count = start + curr['CPU_required']

        #remove the smallest arrival time required entire row from the dataframe
        data = data.drop(curr.name)

        #turnaround time
        turnaround.append(count - start)

        #printing the results
        print("Current Process")
        print(curr)


        #start and finish
        print("Starting Time", start)
        print("Finishing Time", count)

        print("Turnaround Time", turnaround[-1])

    print("Average Turnaround Time", sum(turnaround) / len(turnaround))


def runsjf(data):
    if data.empty:
        print("Sorry, you have no data")
        return

    count = 0
    TripTimes = []
    turnaround = []

    while not data.empty:
        #only consider processes that have already arrived
        ready = data[data['arrival_time'] <= count]

        #if nobody has arrived, the CPU is idle: look at the earliest arrival(s)
        if ready.empty:
            ready = data[data['arrival_time'] == data['arrival_time'].min()]

        #shortest CPU time among the ready processes
        curr = ready.loc[ready['CPU_required'].idxmin()]
        TripTimes.append(curr['CPU_required'])

        #start when the CPU is free AND the process has arrived
        start = max(count, curr['arrival_time'])
        count = start + curr['CPU_required']

        data = data.drop(curr.name)

        turnaround.append(count - curr['arrival_time'])

        print("Current Process")
        print(curr)
        print("Starting Time", start)
        print("Finishing Time", count)
        print("Turnaround Time", turnaround[-1])

    print("Average Turnaround Time", sum(turnaround) / len(turnaround))

def save(data):
    save_name = input("Enter save file name INCLUDING file extension: ") #another user input line, this time for saving the file
    data.to_csv(f'{save_name}', index=False, sep=' ')



def main():
    file_name = input("Enter file name INCLUDING file extension: ") #user input line
    data = pd.read_csv(f'{file_name}', sep=' ', names=['id', 'memory', 'arrival_time', 'CPU_required', 'Quantum', 'ContextSwitch_Penalty'])
    #reads the file that the user provided and saves the columns with easy to remember and understand names
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            result  = check(data)
            print("Valid data!" if result else "Sorry, invalid data :(") #this is a lot more user friendly
            #than just True or False so that is why it is here
        elif choice == 2:
            show(data)
        elif choice == 3:
            add(data)

        elif choice == 4:
            save(data)

        elif choice == 5:
            runfcfs(data)

        elif choice == 6:
            runsjf(data)

        elif choice == 7:
            exit(0)
        else:
            print("Invalid choice. Please try again.") #error correction

main()