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
    print("\n\nCamp Rezi")
    global welcomeW
    welcomeW = tkinter.Tk()
    welcomeW.title("CampRezi Welcome")
    welcomeW.geometry("500x500")
    welcomeW.configure(bg = "#333333")
    wframe = tkinter.Frame(bg = "#333333")

    welcomeLab = tkinter.Label(wframe, text = "Welcome to CampRezi!\n Login or Make an account",bg = "#333333",fg = "#FFFFFF", font=("Ariel",20))
    welcomeBut1 = tkinter.Button(wframe, text = "Login", bg = "#000000",command = login)
    welcomeBut2 = tkinter.Button(wframe, text = "New Account",command= createUsr)

    welcomeLab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=40)
    welcomeBut1.grid(row = 4, column = 0)
    welcomeBut2.grid(row = 4, column = 2)
    wframe.pack()
    welcomeW.mainloop()
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
    welcomeW.destroy()
    loginW = tkinter.Tk()# define login window 
    loginW.title("CampRezi Login") #login window title 
    loginW.geometry("500x500") #window size 
    lframe = tkinter.Frame(bg = "#333333")
    loginW.configure(bg = "#333333")#window color 
    
    loginLabel = tkinter.Label(lframe, text = "Enter your Credietials",bg = "#333333",fg = "#FFFFFF",font=("Ariel",20))# create label in window 
    loginUNT = tkinter.Label(lframe, text = "Username",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    loginPWT = tkinter.Label(lframe, text = "Password",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    loginUN = tkinter.Entry(lframe)
    loginPW = tkinter.Entry(lframe, show="*")
    loginBut = tkinter.Button(lframe, text = "Login")
    back = tkinter.Button(lframe, text = "Back", command=lambda:[loginW.destroy(),welcome()])

    loginLabel.grid(row = 0, column = 0,columnspan=2,pady = 15)
    loginUNT.grid(row=1, column=0,pady=15)
    loginPWT.grid(row=2,column=0)
    loginUN.grid(row=1,column=1)
    loginPW.grid(row=2,column=1,pady = 15)
    loginBut.grid(row=3,column=0,columnspan=2)
    back.grid(row= 4,column=4)


    lframe.pack()
    loginW.mainloop() ### This is a blocking function 
    
    
    accounts = {}
    
    with open("accounts.txt") as auth:
        for line in auth:
            (usr,pw) = line.split()# Create tuple of username/pw combo 
            accounts[(usr)] = pw #break the tuple in to doctiuonary key,value
        pass
    breaker = True
    while breaker == True:
        print("\n Login to a CampRezi account, or type exit to return to main\n")
        cusername = input("Enter your username: ") # Storeing username and password check if user wants to exit 
        if cusername == "exit":
            welcome()
        cpassword = input("Enter your password: ")
        if cusername not in accounts:
            print("\n User not found. Try agian. OR Type Exit to return to the main screen \n")
            time.sleep(1)
        elif accounts[cusername] == cpassword: #checks username and passwrod againsts known good credentails to allow or stop login 
            global auth_usr
            auth_usr = cusername
            global auth_usrInfo
            with open("userinfo.txt","w") as info: #opens the accounts fike to write the new useres accou nt to the master accounts file 
                for line in info:
                    (un,inf) = line.split()
                    auth_usrInfo[un] = inf
            print("\n Login Succesful \n")
            print(auth_usrInfo)
            print("Logged in as", auth_usr,"\n")
            auth.close() # close username and passwrod file
            break
        else:
            print("\n Incorrect Login. Try agian. \n")
            time.sleep(1)
    print(auth_usr,"\n",auth_usrInfo)
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


'''User will be able to view available sites and choose one to reserve, or cancel a reservation '''
def view(): # 
    pass

def reserve(): # reserve will be able to input the day they want to reserve and it will be stored in a dictionary in a file local to the program 
    pass

def cancel():
    pass



welcome()

'''while True:
    print("Hello ",auth_usrInfo['first']," what yould you like to do\n")
    choice = input("View reservations: 'View'\n Create Reservation: 'New'\n Cancel Reselvation: 'Cancel'\n Exit: 'Exit'").lower()
    if choice == "view":
        view()
        continue
    elif choice == "new":
        reserve()
        continue
    elif choice == "cancel":
        cancel()
        continue
    elif choice == "exit":
        welcome()
        break
    else: 
        print("Please enter a valid choice")
        continue
    
'''