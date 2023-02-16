# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DTil, 02.15.2023, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
fileData = None  # Variable to hold raw text file data
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:  # If text file exists, load text file data
    fileData = open(objFile, 'r')
    for row in fileData:  # For each row, store task and priority data
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0].title(), "Priority": lstRow[1].strip().capitalize()}  # Represent each row as dictionary
        lstTable.append(dicRow) # Add each dictionary type data into a list
    fileData.close()  # Close file after storing file data
except:  # Error exception if text file does not exist. Continue with script
    None

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""\n------------------------
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if (len(lstTable) == 0):  # Prompt for an empty list
            print("There are no tasks!")
        else:  # Display each item in the list
            print("Task | Priority")
            for dicData in lstTable:  # Iterate through each dictionary within the list
                print(dicData["Task"], "|", dicData["Priority"])   # Display dictionary in Task | Priority format
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Prompt user to input task and priority
        taskName = input("What is the name of the task you would like to add? ")
        prioName = input("What's the priority of this task? [Low, Medium, High] - ")
        dicRow = {"Task": taskName.title(), "Priority": prioName.capitalize()}  # Process given data into dictionary type
        lstTable.append(dicRow)  # Store user data into list
        print("\nAdded", taskName.title(), "with", prioName.capitalize(), "priority to the list!")  # Print confirmation to user
        continue

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        if (len(lstTable) == 0):  # Skip Remove step if there are no items in the list
            print("There are no tasks available for removal!")
        else:  # Prompt for item removal
            print("List of Tasks for Removal:")
            print("\tTask | Priority")
            count = 0
            for dicData in lstTable:  # Prints list of tasks for user reference
                count += 1  # Counter for numbered listing purposes
                print(count, ".  ", dicData["Task"], " | ", dicData["Priority"], sep='')
            removeTask = input(f'\nWhich task would you like to remove? [1 - {len(lstTable)}] - ')  # User input to select which task to remove
            print("\nRemoved", lstTable[int(removeTask) - 1]["Task"], "from the list!")  # Print confirmation to user
            del lstTable[int(removeTask) - 1]  # Deletes selected task from the list
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        fileData = open(objFile, 'w')  # Open text file in write mode
        for dicData in lstTable:  # Write each dictionary data in the list
            strData = dicData["Task"] + "," + dicData["Priority"] + "\n"  # Convert dict data into readable str
            fileData.write(strData)  # Writes str to text file
        fileData.close()  # Close text file
        print("All tasks has been saved!")  # Print confirmation to user
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        saveConfirm = input("Are you sure you want to quit? [y/n] - ")  # User input to confirm exiting program
        if (saveConfirm.lower() == 'y'):
            print("Closing Program!")  # if yes, end program
            break
        else:  # Otherwise continue the program
            continue