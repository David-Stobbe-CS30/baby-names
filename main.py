# BABY NAMES DATA ASSIGNMENT START CODE

import json

def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.loads(file.read())
    file.close()

    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False



def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***")
    print("* 1: Display All")
    print("* 2: Search by Gender")
    print("* 3: Search by Rank")
    print("* 4: Search by Starting Letter")
    print("* 5: Search by Name Length")
    print("* 6: Exit")

    return input("* Enter Option #: ")

def printList(babies):
    for i in range(len(babies)):
        print(f"{babies[i]['name']} (Rank: {babies[i]['rank']}, Gender: {babies[i]['gender']})")

def displayAll(baby_data):
    # Display All Baby Data
    print("\nDISPLAY ALL")
    printList(baby_data)


def searchGender(baby_data):
    # Dislay All Baby Names based on Gender
    print("\nSEARCH BY GENDER")
    gender = input("Enter a gender (Boy/Girl): ")
    babies = []
    for i in range(len(baby_data)):
        if(baby_data[i]['gender'] == gender):
            babies.append(baby_data[i])
    printList(babies)


def searchRank(baby_data):
    # Display All Baby Names based on Rank
    print("\nSEARCH BY RANK")    
    rank = int(input("Enter a rank: "))
    babies = []
    for i in range(len(baby_data)):
        if(baby_data[i]['rank'] == rank):
            babies.append(baby_data[i])
    printList(babies)

def searchStartLetter(baby_data):
    # Insert User Item into a Position
    print("\nSEARCH BY START LETTER")
    letter = input("Enter a letter: ")
    babies = []
    for i in range(len(baby_data)):
        if(baby_data[i]['name'][0] == letter):
            babies.append(baby_data[i])
    printList(babies)


def searchNameLength(baby_data):
    # Remove item from position
    print("\nSEARCH BY NAME LENGTH")
    length = int(input("Enter length: "))
    babies = []
    for i in range(len(baby_data)):
        if(len(baby_data[i]['name']) == length):
            babies.append(baby_data[i])
    printList(babies)

# Invoke main to begin program
main()
