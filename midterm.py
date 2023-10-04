#!usr/bin/env python3
#Jacob Foppes Midterm- Campsite Reservtions 2.0 - CampRezi

import tkinter
import time
import os
import sys
from pathlib import Path
''' This program will enhace the reservation ysstemn i created for a previous project. It will store reservationa in  a master file. 
The master file will be imported as a dictionary.
EX {2023-05-19:jfoppes, 2023-05-20:jfoppes, 2023-05-30:timmyB}
reservations wikll be appended to the dictionary where created, and popped when removed.
the authenticated user will only be able to pop reservations under thier name 
progrma will use tkinter to create window with picture of campsites 
'''

''' User will authenticate with a username and password or they will create one '''

auth_usr = ""
auth_usrInfo = {} # dictionary of autherized user info 
owd = os.getcwd()

def welcome(): # User greeted with login or create new account option 
    print("\n\nSecure Drive")
    while True: # this while loop will handle user input and call login/ new account functions
        action = input("\nWelcome to CampRezi!\n \n What would you like to do? \n \n Login? or create an account?\n\n Type 'Login' or 'New'\n\n").lower()
        if action == "login":
            login()
            break        
        elif action == "new":
            createUsr()
            break
        elif action == "exit":
            break
        else: 
            print("Please enter a valid choice")
    pass

def login(): #exisiting useres login 
    accounts = {}
    with open("accounts.txt") as auth:
        for line in auth:
            (usr,pw) = line.split()# Create tuple of username/pw combo 
            accounts[(usr)] = pw #break the tuple in to doctiuonary key,value
        pass
    breaker = True
    while breaker == True:
        print("\n Create a CampRezi account \n")
        nusername = input("Create your username: ")
        npassword = input("Create your password: ")
        if nusername in accounts:
            print("Username already taken. Please Choose Another\n")
        else:
            global auth_usr
            auth_usr = nusername
            accounts[nusername] = npassword
            with open("accounts.txt","w") as auth: #opens the accounts fike to write the new useres accou nt to the master accounts file 
                for key, value in accounts.items():
                    auth.write('%s %s\n' % (key, value))
        
            print("Account creation sucessfull. Logged in as:", nusername,"\n")
            break

def createUsr(): # New users create accounts
    accounts = {}
    with open("accounts.txt") as auth:
        for line in auth:
            (usr,pw) = line.split()# Create tuple of username/pw combo 
            accounts[(usr)] = pw #break the tuple in to doctiuonary key,value
        pass
    breaker = True
    while breaker == True:
        print("\n Create a CampReszi account \n")
        nusername = input("Create your username: ")
        npassword = input("Create your password: ")
        if nusername in accounts:
            print("Username already taken. Please Choose Another\n")
        else:
            global auth_usr
            auth_usr = nusername
            accounts[nusername] = npassword
            with open("accounts.txt","w") as auth: #opens the accounts fike to write the new useres accou nt to the master accounts file 
                for key, value in accounts.items():
                    auth.write('%s %s\n' % (key, value))
            print("We need some basic info to finish your account")
            with open("userinfo.txt", "w") as info:
                uInfo = {}
                uInfo['username'] = auth_usr
                uInfo['first'] = input("Enter your first name: ")
                uInfo['last'] = input("Enter your last name: ")
                uInfo['phone'] = input("Enter your phone number with no spaces or dashes: ")
                info.write('%s %s \n' % (auth_usr, uInfo))
                time.sleep(.5)
                global auth_usrInfo
                auth_usrInfo = uInfo
            print("Account creation sucessfull. Logged in as: ", nusername,"\n")
            break
welcome()
while True:
    
    break

'''User will be able to view available sites and choose one to reserve, or cancel a reservation '''
def view(): # 
    pass

def reserve(): # reserve will be able to input the day they want to reserve and it will be stored in a dictionary in a file local to the program 
    pass

def cancel():
    pass

while True: # while look for reservation system
    break