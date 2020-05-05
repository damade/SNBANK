import webbrowser
import math
import string
import random
import re
import pprint

# This is the container containing user data, I am using the Data Structure Dictionary as container
hngAccounts = {'damilola5@gmail.com': {'password': 'dammy', 'first_name': 'Damilola', 'last_name': 'Adeoye'}}

# It  is the regex expression from inbuilt function "re" to verify the email address is a valid one
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

""""#It solves Task 2 by generating a Random password
through first and last name including the random generated characters"""

"""This function handles the home page"""
def homePage():
    print("\n-------------------------------------------------------WELCOME TO SNG BANK-------------------------------------------------------\n")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HOME PAGE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("Kindly use the key '1' or '2' to navigate through\n")
    print("1. STAFF LOGIN:")
    print("2. CLOSE APP")


    promptQuestion = int(input("Reply: "))
    if (promptQuestion == 1):
        staffLogin()
    elif (promptQuestion == 2):
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
    print("\n<=<=<=<=<=NOTE THAT YOUR EMAIL MUST HAVE THE DOMAIN 'snb.com'=>=>=>=>=>\n")
    staffUserName = input("Enter email address: ").lower()
    staffPassword = input("Enter password: ")
    if staffUserName in hngAccounts.keys():
        if hngAccounts[staffUserName]['password'] == staffPassword:
            print("You're logged in\n")
            pprint.pprint(hngAccounts[staffUserName])
            staffName = "Damilola Adeoye"
            staffPortal(staffUserName,staffName)
        else:
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
    print(f"\nWelcome back {name}!\nHow may i help?")
    print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
    print("1. Create new bank account")
    print("2. Check account details")
    print("3. Logout\n")
    promptQuestion = input("Reply: ")
    if (promptQuestion == '1'):
        createAccount()
    elif (promptQuestion == '2'):
        checkAccountDetails()
    elif (promptQuestion == '3'):
        print(f"Thank you {name}, bye for now")
        staffLogin()
    else:
        exit()

def createAccount():
    accountList = ["Savings","Current","Business", "Domiciliary", "Fixed"]
    print("\n-------------------------- CREATE NEW ACCOUNT --------------------------")
    print("Kindly fill the details below\n")
    userAccountName = input("What is your full name: ")
    userOpeningBalance = int(input("What amouunt is been used: "))
    print("\nSelect your type of Account below")
    print("1. Savings\n2. Current\n3. Business\n4. Domiciliary\5. Fixed")
    userAccountType = accountList[int(input("Fill it here.")) - 1]
    userEmail = input("Enter a valid email address: ").lower();
    if (re.search(regex, userEmail)):
        if verifyAccount(userEmail):
            print("Email Address Already exists! Try again")
            homeAnyOther()
        else:
            domain = userEmail.split('@')[1]
            if domain == "hng.tech.com":
                first_name = input("Enter your first name: ").lower()
                last_name = input("Enter your last name: ").lower()
                PasswordConfirmation(userEmail, first_name, last_name)
            else:
                print("Invalid Email Address Domain\nKindly enter the company's domain")
                createAccount()
    else:
        print("Invalid Email Address")
        createAccount();


def checkAccountDetails():
    checkForDetails = "thank you for now"
    userAccountNumber = input("What is your Account Number? ")
def AccountGenerator():
    accountPrefix = ["00","01"]
    suffixGen = random.randrange(10000000,99999999)
    randomPrefixGen = random.randint(0,1)
    finalAccount = accountPrefix[randomPrefixGen] + str(suffixGen)
    return finalAccount  # releases the output of the input


def PasswordGenerator(first_name, last_name):
    size = 5
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase  # specifies the type of chracter needed through ASCII
    randomString = ''.join(random.choice(chars) for _ in range(size))
    finalPassword = first_name[0:2] + last_name[-2:] + randomString
    return finalPassword  # releases the output of the input


"""Takes care of the second part of Task 4
By verifying that the length is of length 7 or above 
"""


def PersonalizedPasswordGenerator(newEmail, first_name, last_name):
    newPassword = input("Enter a valid password of length 7 and above : ")
    if ((len(newPassword)) >= 7):
        confirmNewPassword = input("Confirm password for entry: ")
        if (newPassword == confirmNewPassword):
            hngAccounts[newEmail] = {'password': newPassword, 'first_name': first_name, 'last_name': last_name}
            print("Your account has been created successfully!")
            print("\nKindly Login to confirm your sign-up")
            authenticateUser()  # Log-in page function
        else:
            PersonalizedPasswordGenerator(newEmail, first_name, last_name)
    else:
        print("\nInput a password that is above length 7")
        PersonalizedPasswordGenerator(newEmail, first_name, last_name)


"""Takes care of Task 3, by populating the Random Password Generated.
Asks the User for permission to use it ........"""


def PasswordConfirmation(newEmail, first_name, last_name):
    password = PasswordGenerator(first_name, last_name);
    print("Your password is " + password)
    reply = input("Are you satisfied with it? Y/N ")
    if (reply.lower() == 'y'):
        hngAccounts[newEmail] = {'password': password, 'first_name': first_name, 'last_name': last_name}
        print("Your account has been created successfully!\n")
        pprint.pprint(hngAccounts[newEmail])
        print("\nKindly Login to confirm your sign-up")
        authenticateUser()
    elif (reply.lower() == 'n'):
        PersonalizedPasswordGenerator(newEmail, first_name, last_name)
    else:
        createAccount()
    return


"""It is the function used to create account for new employees"""








"""This function verifies that an email is stored in our container(database)"""


def verifyAccount(email):
    if email in hngAccounts.keys():
        return email
    return False


"""This function handles the Log-In page"""


def authenticateUser():
    print("\n--------------------------LOG IN--------------------------")
    print("\n<=<=<=<=<=NOTE THAT YOUR EMAIL MUST HAVE THE DOMAIN 'hng.tech.com'=>=>=>=>=>\n")
    userEmail = input("Enter email address: ").lower()
    userPassword = input("Enter password: ")
    if userEmail in hngAccounts.keys():
        if hngAccounts[userEmail]['password'] == userPassword:
            print("You're logged in\n")
            pprint.pprint(hngAccounts[userEmail])
            homeAnyOther()

    else:
        print("You are not authorized!\nWrong Email or password!!!")
        print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
        print("1. Do you want to attempt the log in again?")
        print("2. Do you want to return to home page?")
        print("3. Do you want to open an Account with us\n")
        promptQuestion = input("Reply: ")
        if (promptQuestion == '1'):
            authenticateUser()
        elif (promptQuestion == '2'):
            homePage()
        elif (promptQuestion == '3'):
            createAccount()
        else:
            exit()







# Creates an infinite loop to run the program
# It also handles Task 5
var = 1
while var == 1:
    homePage()
