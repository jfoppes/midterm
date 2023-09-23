#!usr/bin/env python3
from tkinter import *
from tkinter import ttk 
import time
root = Tk()
frm  = ttk.Frame(root, padding=10)
frm.grid()

sitefile = open("allsites.txt", "r") #open al sites files
allsitesd = sitefile.read() # read all sirtes filles#
allsites = allsitesd.split("\n") # create lsit of all sites file deliented at the "return"

resfile = open("reserved.txt", "r")
reservedd = resfile.read()
reserved = reservedd.split("\n")

availfile = open("available.txt", "r")
availablee = availfile.read()
available = availablee.split("\n")


choice = ""

print(allsites)
def reserve():
        root1 = Tk()
        frmres  = ttk.Frame(root1, padding=10)
        frmres.grid()
        def get_entry():
            print(usrinput.get())
            choice = usrinput.get()
            while True:
                valid = available.count(usrinput)
                if valid > 0:
                    pass
                else:
                    print("Please choose an available site")
                if usrinput in available:
                    available.remove(usrinput) # add reservation to list 
                    reserved.append(usrinput) #remove reservatio nfrom avialable 
                    print("Reserved Sites:\n" , reserved)
                    print("Available Sites:\n" , available)
                    time.sleep(1)
                if valid > 0:
                    pass
                else:
                    print("Please choose an available site")
                if usrinput in available:
                    available.remove(usrinput) # add reservation to list 
                    reserved.append(usrinput) #remove reservatio nfrom avialable 
                    print("Reserved Sites:\n" , reserved)
                    print("Available Sites:\n" , available)
                time.sleep(1)
                another = input("Would you like to reserve another site?\n").lower()
                if another == "yes":
                    continue
                elif another== "no":
                    break
                else:
                    print("Please enter a valid choice")
        usrinput = ttk.Entry(frmres,)
        usrinput.grid(column=3, row=4)
        ttk.Button(frmres, text="Submit",command=get_entry).grid(column=4, row=4)  
        ttk.Label(frmres, text="Enter site selection here").grid(column=3, row=3)
        ttk.Label(frmres, text="The following sites are available:").grid(column=1,row=1)
        ttk.Label(frmres,text=available).grid(column=2,row=2)
        reservation=input(" Which Site would you like to reserve?\n")
        valid = available.count(reservation)
def cancel():
    while True:
        print("\n\nThe following sites are reserved: \n")
        for i in reserved:
            print(i) 
        cancelation =input("Which reservation would you like to cancel?\n")
        reserved.remove(cancelation) # add reservation to list 
        available.append(cancelation) #remove reservatio nfrom avialable 
        print("Reserved Sites:\n" , reserved)
        print("Available Sites:\n" , available)
        time.sleep(1)
        another = input("Would you like to cancel another site?\n").lower()
        if another == "yes":
            continue
        elif another== "no":
            break
        else:
            print("Please enter a valid choice")
def view():  
    print("\n Our location is home to the follwowing sites\n", allsites)
    print("\nThe following sites are avaialbe",available)
    print("\n The Following Sites are reserved\n",reserved)
    time.sleep(1)
    
    
ttk.Label(frm, text="Welcome to Reservations").grid(column=0, row=0)
ttk.Button(frm, text="Reserve", command=reserve).grid(column=1, row=1)
ttk.Button(frm, text="View Reservations", command=view).grid(column=1, row=2)
ttk.Button(frm, text="Cancel Reservations", command=cancel).grid(column=1, row=3)



ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=0)

root.mainloop()
