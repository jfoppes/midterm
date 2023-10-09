#!usr/bin/env python3
#Jacob Foppes Midterm- Campsite Reservtions 2.0 - CampRezi

import tkinter
import time
import os
import sys
from pathlib import Path
import json
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

def loby():
    lobyW = tkinter.Tk()
    lobyW.title("CampRezi Welcome")
    lobyW.geometry("500x500")
    lobyW.configure(bg = "#333333")
    lobframe = tkinter.Frame(bg = "#333333")

    lobLab = tkinter.Label(lobframe, text = ("Hello "+ auth_usrInfo['first']+"!\n\nWelcome to CampRezi,\n Login or Make an account"),bg = "#333333",fg = "#FFFFFF", font=("Ariel",20))
    lobBut1 = tkinter.Button(lobframe, text = "View Available Sites", bg = "#000000",command = view)
    lobBut2 = tkinter.Button(lobframe, text = "New Reservation",command= reserve)
    lobBut3 = tkinter.Button(lobframe, text = "Cancel Reservation",command= cancel)
    back = tkinter.Button(lobframe, text = "Back", command=lambda:[lobyW.destroy(),welcome()])
    
    lobLab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=40)
    lobBut1.grid(row = 2, column = 1)
    lobBut2.grid(row = 3, column = 1,pady = 10)
    lobBut3.grid(row = 4, column = 1)
    back.grid(row= 5,column=4)
    lobframe.pack()
    lobyW.mainloop()

def welcome(): # User greeted with login or create new account option 
    print("\n\nCamp Rezi")
    global auth_usr 
    global auth_usrInfo
    auth_usr = ""
    auth_usrInfo = {}
    
    global welcomeW
    welcomeW = tkinter.Tk()
    welcomeW.title("CampRezi Welcome")
    welcomeW.geometry("500x500")
    welcomeW.configure(bg = "#333333")
    wframe = tkinter.Frame(bg = "#333333")

    welcomeLab = tkinter.Label(wframe, text = "Welcome to CampRezi!\n Login or Make an account",bg = "#333333",fg = "#FFFFFF", font=("Ariel",20))
    welcomeBut1 = tkinter.Button(wframe, text = "Login", bg = "#000000",command =lambda:[welcomeW.destroy(),login()])
    welcomeBut2 = tkinter.Button(wframe, text = "New Account",command= lambda: [welcomeW.destroy(),createUsrWin()])

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

def login(): #exisiting useres login window
    global loginW
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
   # print(cusername,cpassword)
    loginBut = tkinter.Button(lframe, text = "Login",command=lambda: [chklogin(loginUN.get(),loginPW.get()),loginW.destroy()])
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
def chklogin(cusername,cpassword): # checks login credntials 
    #print(cusername,cpassword)
    accounts = {}
    with open("accounts.txt") as auth:
        for line in auth: 
            (usr,pw) = line.split()# Create tuple of username/pw combo 
            accounts[(usr)] = pw #break the tuple in to doctiuonary key,value
        pass
    print("\n Login to a CampRezi account, or type exit to return to main\n")
    if cusername not in accounts:
        loginW.destroy()
        error("Looks look that account does not exit, try agin!")
        login()
    elif accounts[cusername] == cpassword: #checks username and passwrod againsts known good credentails to allow or stop login 
        global auth_usr
        auth_usr = cusername
        global auth_usrInfo
        with open("userinfo.txt","r") as info: #opens the accounts fike to read the new accoun t info
            users = {} 
            for line in info: # reading user info file and adding it to dict of users:userinfo
                line = line.replace("\'", "\"")
                (un,inf) = line.split(" ", 1)
                inf = json.loads(inf) #intitate the values in inf as dict insterad of string
                users[(un)] = inf #string key in the dictionary users has value of the inf dicationary for that user 
            for cusername in users: # for the authenticated user: find thier entry in the users DICT and make it that authorized user info
                (un,inf) = line.split(" ", 1)
                inf = json.loads(inf)
                auth_usrInfo = inf            
        print("\n Login Succesful \n")
        print("Logged in as", auth_usr,"\n")
        auth.close() # close username and passwrod file
        loginW.destroy()
        loby()
    else:
        loginW.destroy()
        error("Wrong password try agin!")
        login()
    
def createUsrWin(): # New users create accounts
    global mkaccW
    mkaccW = tkinter.Tk()# define login window 
    mkaccW.title("CampRezi New User") #login window title 
    mkaccW.geometry("500x500") #window size 
    mkaccframe = tkinter.Frame(bg = "#333333")
    mkaccW.configure(bg = "#333333")#window color 
    
    mkaccLabel = tkinter.Label(mkaccframe, text = "Let Make you an Account!",bg = "#333333",fg = "#FFFFFF",font=("Ariel",20))# create label in window 
    mkaccLabel2 = tkinter.Label(mkaccframe, text = "Enter your information below",bg = "#333333",fg = "#FFFFFF",font=("Ariel",16))
    newFirstT =  tkinter.Label(mkaccframe, text = "First Name",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newLastT =  tkinter.Label(mkaccframe, text = "Last Name",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newNumT =  tkinter.Label(mkaccframe, text = "Phone Number",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newUNT = tkinter.Label(mkaccframe, text = "Username",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newPWT = tkinter.Label(mkaccframe, text = "Password",bg = "#333333",fg = "#FFFFFF",font=("Ariel",14))
    newFirst = tkinter.Entry(mkaccframe)
    newLast = tkinter.Entry(mkaccframe)
    newNum = tkinter.Entry(mkaccframe)
    newUN = tkinter.Entry(mkaccframe)
    newPW = tkinter.Entry(mkaccframe, show="*")
   # print(cusername,cpassword)
    loginBut = tkinter.Button(mkaccframe, text = "Login",command=lambda: [createUsr(newFirst.get(),newLast.get(),newNum.get(),newUN.get(),newPW.get()),mkaccW.destroy(),loby()])
    back = tkinter.Button(mkaccframe, text = "Back", command=lambda:[mkaccW.destroy(),welcome()])

    mkaccLabel.grid(row = 0, column = 0,columnspan=2,pady = 15)
    mkaccLabel2.grid(row = 1, column = 0,columnspan=2,pady = 15)
    newFirstT.grid(row=2, column=0,pady=15)
    newLastT.grid(row=3, column=0)
    newNumT.grid(row=4, column=0,pady=15)
    newUNT.grid(row=5, column=0)
    newPWT.grid(row=6,column=0,pady =15 )
    newFirst.grid(row=2,column=1)
    newLast.grid(row=3,column=1,pady=15)
    newNum.grid(row=4,column=1)
    newUN.grid(row=5,column=1,pady = 15)
    newPW.grid(row=6,column=1)
    loginBut.grid(row=7,column=0,columnspan=2)
    back.grid(row= 8,column=4)
    mkaccframe.pack()
    
    mkaccW.mainloop()
def createUsr(first,last,num,un,pasw):  
    accounts = {}
    with open("accounts.txt") as auth:
        for line in auth:
            (usr,pw) = line.split()# Create tuple of username/pw combo 
            accounts[(usr)] = pw #break the tuple in to doctiuonary key,value
        pass
    breaker = True
    while breaker == True:
        nusername = un
        npassword = pasw
        if nusername in accounts:
            mkaccW.destroy()
            error("Looks look that account already exits, try agin!")
            createUsrWin()
        else:
            global auth_usr
            auth_usr = nusername
            accounts[nusername] = npassword
            with open("accounts.txt","w") as auth: #opens the accounts fike to write the new useres accou nt to the master accounts file 
                for key, value in accounts.items():
                    auth.write('%s %s\n' % (key, value))
            with open("userinfo.txt", "a") as info:
                uInfo = {}
                uInfo['username'] = auth_usr
                uInfo['first'] = first
                uInfo['last'] = last
                uInfo['phone'] = num
                info.write('%s %s\n' % (auth_usr, uInfo))
                time.sleep(.5)
                global auth_usrInfo
                auth_usrInfo = uInfo
            print("Your Info : \n Name: ", auth_usrInfo["first"],auth_usrInfo["last"], "\nContact Numnber: ", auth_usrInfo['phone'])
            print("Account creation sucessfull. Logged in as: ", auth_usrInfo['username'],"\n")
            break


'''User will be able to view available sites and choose one to reserve, or cancel a reservation '''
def view(): # 
    print("View Reservations:")
    

def reserve(): # reserve will be able to input the day they want to reserve and it will be stored in a dictionary in a file local to the program 
    print("New Reservation ")

def cancel():
    print("Cancel Reservation ")

def error(message):
    errorW = tkinter.Tk()
    errorW.title("OOPS!")
    errorW.geometry("")
    errorW.configure(bg = "#333333")
    eframe = tkinter.Frame(bg = "#333333")

    errorlab= tkinter.Label(eframe, text = message,bg = "#333333",fg = "#FFFFFF", font=("Ariel",20))
    okBut = tkinter.Button(eframe, text = "Try again.",command= errorW.destroy)

    errorlab.grid(row = 0, column = 0,columnspan= 2, sticky = "news",pady=20,padx = 30)
    okBut.grid(row = 1, column = 0,pady=20,padx=40)
    eframe.pack(expand = True, fill="both")
    errorW.mainloop()

welcome()

'''
    
'''