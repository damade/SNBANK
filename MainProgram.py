import webbrowser
import math
import string
import random
import re
import pprint
import time
import os

# It  is the regex expression from inbuilt function "re" to verify the email address is a valid one
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

""""#It solves Task 2 by generating a Random password
through first and last name including the random generated characters"""

"""This function handles the home page"""


def homePage():
    print(
        "\n-------------------------------------------------------WELCOME TO SNG BANK-------------------------------------------------------\n")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HOME PAGE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("Kindly use the key '1' or '2' to navigate through\n")
    print("1. STAFF LOGIN:")
    print("2. CLOSE APP")

    promptQuestion = input("Reply: ")
    if (promptQuestion == '1'):
        staffLogin()
    elif (promptQuestion == '2'):
        exit()
    else:
        print("Enter a valid option")
        homeAnyOther()


"""The function that handles Other Operations in the program especially the Log-in page"""


def homeAnyOther():
    print("\n-------------------------- KINDLY CHOOSE WHAT NEXT --------------------------\n")
    print("1. Do you want to return to home page?")
    print("2. Do you want to exit\n")
    promptQuestion = input("Reply: ")
    if (promptQuestion == '1'):
        homePage()
    elif (promptQuestion == '2'):
        exit()
    else:
        exit()


def staffLogin():
    print("\n--------------------------LOG IN--------------------------")
    print("\n<=<=<=<=<=NOTE THAT YOUR DETAILS ARE SECURE=>=>=>=>=>\n")
    staffUserName = input("Enter username: ").lower()
    staffPassword = input("Enter password: ")
    searchfile = open(r'DataFolder\staff.txt', "r")
    for line in searchfile:
        if staffUserName in line:
            theString = line
            password = theString.split(" ")[1]
            if staffPassword == password:
                print("You're logged in\n")
                staffName = theString.split(" ")[3] + " " + theString.split(" ")[4]
                searchfile.close()
                staffPortal(staffUserName, staffName)
            else:
                searchfile.close()
                print("You are not authorized!\nWrong Password!!!")
                print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
                print("1. Do you want to attempt the log in again?")
                print("2. Do you want to return to home page?")
                promptQuestion = input("Reply: ")
                if (promptQuestion == '1'):
                    staffLogin()
                elif (promptQuestion == '2'):
                    homePage()
                else:
                    print("Invalid Input")
                    exit()
        else:
            searchfile.close()
            print("You are not authorized!\nWrong Email!!!")
            print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
            print("1. Do you want to attempt the log in again?")
            print("2. Do you want to return to home page?")
            promptQuestion = input("Reply: ")
            if (promptQuestion == '1'):
                staffLogin()
            elif (promptQuestion == '2'):
                homePage()
            else:
                print("Invalid Input")
                exit()



def staffPortal(userName, name):
    print("\n--------------------------STAFF PORTAL--------------------------")
    baconFile = open('DataFolder\\UserSession.txt', 'w')
    ts = time.gmtime()
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    userSessionText = name.upper() + " with username " + userName + " logged in at about the time " + currentTime + " GMT\n"
    baconFile.write(userSessionText)
    baconFile.close()
    print(f"\nWelcome back {name}!\nHow may i help?")
    print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
    print("1. Create new bank account")
    print("2. Check account details")
    print("3. Logout\n")
    promptQuestion = input("Reply: ")
    if (promptQuestion == '1'):
        createAccount(userName, name)
    elif (promptQuestion == '2'):
        checkAccountDetails(userName, name)
    elif (promptQuestion == '3'):
        print(f"\nThank you {name}, bye for now")
        os.remove(r"DataFolder\UserSession.txt")
        staffLogin()
    else:
        os.remove(r"DataFolder\UserSession.txt")
        exit()


def createAccount(userName, name):
    accountList = ["Savings", "Current", "Business", "Domiciliary", "Fixed"]
    print("\n-------------------------- CREATE NEW ACCOUNT --------------------------")
    print("Kindly fill the details below\n")
    userAccountFirstName = input("What is your first name: ")
    userAccountLastName = input("What is your last name: ")
    userAccountThirdName = input("What is your third name: ")
    userBalance = int(input("What amount is been used to open: "))
    print("\nSelect your type of Account below")
    print("1. Savings\n2. Current\n3. Business\n4. Domiciliary\n5. Fixed")
    userAccountType = accountList[int(input("\nFill it here. ")) - 1]
    userEmail = input("Enter a valid email address: ").lower();
    if (re.search(regex, userEmail)):
        userAccountNumber = AccountGenerator()
        CustomerFile = open('DataFolder\\customer.txt', 'a')
        customerData = userAccountNumber + " " + str(userBalance) + " " + userAccountFirstName + " " + userAccountThirdName + " " + \
                       userAccountLastName + " " + userEmail + " " + userAccountType + "\n"
        CustomerFile.write(customerData)
        CustomerFile.close()
        print(f"\n{userAccountFirstName} {userAccountLastName} just opened a {userAccountType} account with SNB\n"
              f"Your Account number is {userAccountNumber} with #{userBalance:,} balance")
        staffPortal(userName, name)
    else:
        print("Invalid Email Address")
        createAccount(userName, name)


def checkAccountDetails(userName,name):
    print("\n-------------------------- CHECK ACCOUNT DETAILS --------------------------")
    userAccountNumber = input("What is your Account Number? ")
    CustomerSearchfile = open(r'DataFolder\customer.txt', "r")
    for line in CustomerSearchfile:
        if userAccountNumber in line:
            theString = line
            customerAccountBalance = int(theString.split(" ")[1])
            customerAccountName = theString.split(" ")[2].capitalize()+" " + theString.split(" ")[3].capitalize() + " " + theString.split(" ")[4].capitalize()
            customerAccountEmail = theString.split(" ")[5]
            customerAccountType = theString.split(" ")[6]
            print(f"\nAccount Number: {userAccountNumber}\nAccount Name: {customerAccountName}\n"
                  f"Account Balance: #{customerAccountBalance:,}\nAccount Type: {customerAccountType}\n"
                  f"Account Email: {customerAccountEmail}")
            CustomerSearchfile.close()
            staffPortal(userName, name)
        else:
            print("\nYou are not authorized!\nAccount Number!!!")
            CustomerSearchfile.close()
            staffPortal(userName, name)



def AccountGenerator():
    accountPrefix = ["00", "01"]
    size = 8
    chars = string.digits  # specifies the type of chracter needed through ASCII
    randomString = ''.join(random.choice(chars) for _ in range(size))
    randomPrefixGen = random.randint(0, 1)
    finalAccount = accountPrefix[randomPrefixGen] + randomString
    return finalAccount  # releases the output of the input


# Creates an infinite loop to run the program
# It also handles Task 5
print("Follow the format in the staff.txt file to create and authenticate staff permission")
var = 1
while var == 1:
    homePage()
