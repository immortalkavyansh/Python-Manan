"""
Imports
"""
from tkinter import *
import datetime
import random
import tkinter.messagebox as message
import os
import smtplib
import pyttsx3

"""
Speak Function
"""
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

"""
Function To Clear Data
"""
def cleardata():
    #Clearing Check-in FIle
    f = open("Hotel Check In List.txt", "w")
    f.write("")

    #CLearing Check-out file
    ff = open("Hotel Check Out List.txt", "w")
    ff.write("")

    #Clearing feedback file
    fff = open("User FeedBack HMS.txt", "w")
    fff.write("")
    
    #Clearing Guest list
    ffff = open("Guest List.txt", "w")
    ffff.write("")

"""
HomePage Function
"""

def homepage():
    global root_homepage
    root_homepage = Tk()
    root_homepage.geometry("549x444")
    root_homepage.title("PythonWithManan - Hotel")
    root_homepage.config(bg="peach puff")

    #Title Of The GUI
    Label(root_homepage, text="Welcome To PythonWithManan-Hotel", font="algerian 20 bold", bg="orange red").grid(row=1, column=0)
    Label(root_homepage, text="Welcome To PythonWithManan-Hotel", font="algerian 20 bold", bg="peach puff", fg="peach puff").grid(row=7, column=0)

    #Buttons
    checkin = Button(root_homepage, text="Check IN", font="comicsansMS 20 bold", bg="cyan", command=checkinbutton)
    checkin.grid(row=2, column=0)

    checkout = Button(root_homepage, text="Check OUT", font="comicsansMS 20 bold", bg="cyan", command=checkoutbutton)
    checkout.grid(row=3, column=0)

    guestlist = Button(root_homepage, text="Guest List", font="comicsansMS 20 bold", bg="cyan", command=GuestList)
    guestlist.grid(row=4, column=0)

    exitbutton = Button(root_homepage, text="Exit/Quit", font="comicsansMS 20 bold", bg="slate blue", command=quit)
    exitbutton.grid(row=6, column=0)

    guestststus = Button(root_homepage, text="Guest Status", font="comicsansMS 20 bold", bg="cyan", command=Gueststatus)
    guestststus.grid(row=5, column=0)

    # cleardatabutton = Button(root_homepage, text="Clear Data", font="comicsansMS 20 bold", bg="slate blue", command=cleardata)
    # cleardatabutton.grid(row=7, column=0)

    Label(root_homepage, text="Hotel Management By\nPythonWithManan", font="comicsansMS 25 bold", bg="lawn green").grid()
    root_homepage.mainloop()

"""
Supportive Functions --- Starts
"""

#Button For Check-in
def checkinbutton():
    root_homepage.destroy()
    checkIn()

#Button For Room Key
def okbutton():
    root_list.destroy()
    homepage()

#Button for Quiting Check-in
def quitcheckin():
    root.destroy()
    homepage()

#Button for Feedback
def feedbackbutton():
    #If discription is empty
    if othervalue.get() == "":
        othervalue.set("None")

    #If feedack is not checked
    if var_feedback.get() == "FeedBack":
        var_feedback.set("None")

    with open("User FeedBack HMS.txt", "a") as f:
        f.write(f"Name - {name_outvalue.get()}\nFeedBack - {var_feedback.get()}\nDiscription - {othervalue.get()}\n---------------------------------------------------\n")
        feedback_root.destroy()
        message.showinfo("Thank You", "Thanyou For You FeedBack.")
        homepage()

#Button for Quitting user status
def exitgueststatus():
    status_root.destroy()
    homepage()

#Function For Quitting check-out
def exitcheck_out():
    root_out.destroy()
    homepage()


"""
Supportive Functions --- Ends
"""

#---------------------------------------------------------------------------------------------------------------

"""
Check IN Function
"""

def checkIn():
    global root
    root = Tk()
    root.configure(bg="light blue")
    root.geometry("850x510")
    root.title("PythonWithManan - Hotel Management")

    var2 = StringVar()
    var2.set("Payment")

    #Text for our form
    Label(root, text="Please fill The Form To Check IN:- ", font="comicsansms 25 bold", bg="light green").grid(row=0, column=2)
    name = Label(root, text="Name (Full Name)", fg="red", font="classic 20 underline").grid(row=1, column=2)
    email = Label(root, text="Email", fg="red", font="classic 20 underline").grid(row=2, column=2)
    phone = Label(root, text="Phone Number", fg="red", font="classic 20 underline").grid(row=3, column=2)
    gender = Label(root, text="Gender", fg="red", font="classic 20 underline").grid(row=4, column=2)
    aadhar = Label(root, text="Aadhar Number", fg="red", font="classic 20 underline").grid(row=5, column=2)
    Label(root, text="Number of Days", fg="red", font="classic 20 underline").grid(row=6, column=2)
    Thanks = Label(root, text="Thanks for visiting our Hotle", fg="light blue", bg="light blue", font="classic 17 bold").grid(row=7, column=2)


    #Payment Mode
    Label(root, text="Payment Mode:- ", font="normal 20", bg="black", fg="white").grid(row=8, column=2)

    payment = Radiobutton(root, text="Google Pay?", variable = var2, pady="5", font="normal 12", value="Google Pay")
    payment.grid(row=9, column=2)
    payment = Radiobutton(root, text="Credit Card?", variable = var2, pady="5", font="normal 12", value="Credit Card")
    payment.grid(row=10, column=2)
    payment = Radiobutton(root, text="Cash?", variable = var2, pady="5", font="normal 12", value="Cash")
    payment.grid(row=11, column=2)

    # Tkinter variable for storing entries
    global namevalue
    global gendervalue
    namevalue = StringVar()
    phonevalue = IntVar()
    gendervalue = StringVar()
    emailvalue = StringVar()
    aadharvalue = IntVar()
    # paymentmodevalue = StringVar()
    daysvalue = IntVar()

    var = StringVar()
    var.set("Room")

    #Entries for our form
    nameentry = Entry(root, textvariable=namevalue, font="normal 20")
    phoneentry = Entry(root, textvariable=phonevalue, font="normal 20")
    genderentry = Entry(root, textvariable=gendervalue, font="normal 20")
    emailentry = Entry(root, textvariable=emailvalue, font="normal 20")
    aadharentry = Entry(root, textvariable=aadharvalue, font="normal 20")
    daysentry = Entry(root, textvariable=daysvalue, font="normal 20")
    # paymentmodeentry = Entry(root, textvariable=paymentmodevalue, font="normal 20")

    # Packing the Entries
    nameentry.grid(row=1, column=3)
    phoneentry.grid(row=3, column=3)
    genderentry.grid(row=4, column=3)
    emailentry.grid(row=2, column=3)
    aadharentry.grid(row=5, column=3)
    daysentry.grid(row=6, column=3)
    # paymentmodeentry.grid(row=5, column=3)

    #Checkbox & Packing it
    Label(root, text="Which Room:- ", font="normal 20", bg="black", fg="white").grid(row=8, column=3)
    room = Radiobutton(root, text="Delux Room?", variable = var, pady="5", font="normal 12", value="Delux Room")
    room.grid(row=9, column=3)
    room = Radiobutton(root, text="Super Delux Room?", variable = var, pady="5", font="normal 12", value="Super Delux Room")
    room.grid(row=10, column=3)
    room = Radiobutton(root, text="Normal Room?", variable = var, pady="5", font="normal 12", value="Normal Room")
    room.grid(row=11, column=3)
    
    """
    Telling user how much he/she has to pay.
    """
    def showpayment():
        checkentry()

        if daysvalue.get() >30:
            message.showerror("Too many Days", "Dear User\nYou have entered more than 30\ndays our limit is 30 days only\nplease rewrit information.")
            root.destroy()
            checkIn()

        else:
            if var.get() == "Normal Room":
                roomtype_value = 3763
                amount = daysvalue.get()*roomtype_value
                message.showinfo("Payment", f"Dear User, \nPLease pay rupees {amount} to check in.\nYour room is {var.get()}\nIf you want so you can extend your days.\nThank you, \nPythonWithManan[Hotel Owner]")
                getvals()
                root.destroy()
                homepage()

            elif var.get() == "Delux Room":
                roomtype_value = 4811
                amount = daysvalue.get()*roomtype_value
                message.showinfo("Payment", f"Dear User, \nPLease pay rupees {amount} to check in.\nYour room is {var.get()}\nIf you want so you can extend your days.\nThank you, \nPythonWithManan[Hotel Owner]")
                getvals()
                root.destroy()
                homepage()

            elif var.get() == "Super Delux Room":
                roomtype_value = 6221
                amount = daysvalue.get()*roomtype_value
                message.showinfo("Payment", f"Dear User, \nPLease pay rupees {amount} to check in.\nYour room is {var.get()}\nIf you want so you can extend your days.\nThank you, \nPythonWithManan[Hotel Owner]")
                getvals()
                root.destroy()
                homepage()


    """
    Sending email
    """
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('mananmaheshwari9548@gmail.com', 'mananchoithram@9548')
        server.sendmail('mananmaheshwari9548@gmail.com', to, content)
        server.close()
        
    """
    Varifying Checkin Entry
    """
    def checkentry():
        try:
            content = f"Dear User({namevalue.get()}),\nYou have checked in to our hotel.\nThankyou for coming our hotel hope you will enjoy.\nPythonWIthManan[Hotel Owner]"
            to = emailvalue.get()
            sendEmail(to, content)
            print("Email Have Been Sent")
            # speak("Email have been sent")

        except Exception as error:
            print(error)
            print("Sorry sir Manan. I am not able to send this email")

        if namevalue.get()=="" or phonevalue.get()=="" or gendervalue.get()=="" or emailvalue.get()=="" or aadharvalue.get()=="":
            message.showerror("Incompleate Information", "Sir/Maam you have submited incompleate\ninformation please compleate it kindly.\nPythonWithManan[Hotel Owner]")
            root.destroy()
            checkIn()
        else:
            pass
    
    """
    Saving User Information
    """

    def getvals():
        if namevalue.get()=="" or phonevalue.get()=="" or gendervalue.get()=="" or emailvalue.get()=="" or aadharvalue.get()=="":
            checkentry()

        else:
            #Getting Todays date
            from datetime import date
            today = date.today()

            current_date = today.strftime("%B %d, %Y")

            #Getting Current Time
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            print("Submitting Form Sir/Maam")

            with open("Guest List.txt", "a") as f:
                f.write(f"Name - {namevalue.get()}\nGender - {gendervalue.get()}\nDate - {current_date}\n-----------------------------------------------------------------------------------------\n")

            print(f"{namevalue.get(), phonevalue.get(), gendervalue.get()}",
                f"{emailvalue.get(), var2.get(), var.get(), current_date}")

            with open("Hotel Check In List.txt", "a") as f:
                f.write(f"\nName - {namevalue.get()}\nMobile Number - {phonevalue.get()}\nGender - {gendervalue.get()}\nEmail - {emailvalue.get()}\nAadhar Number - {aadharvalue.get()}\nPayment Mode - {var2.get()}\nRoom Type - {var.get()}\nDate - {current_date}\nTime - {current_time}\nDays - {daysvalue.get()}\n")

            root.destroy()
            roomkey()


    #Button & packing it and assigning it a command
    Button(root, text="Submit", command=showpayment, bg="red", fg="yellow", pady="5", font="normal 15").grid(row=12, column=3)
    Button(root, text="Quit", command=quitcheckin, bg="red", fg="yellow", pady="5", font="normal 15").grid(row=12, column=2, ipadx=13)

    root.mainloop()

"""
#RoomKey Genrator Function
"""

global room_key
room_key = random.randint(100, 1000)
def roomkey():
    global root_list
    root_list = Tk()
    root_list.config(bg="pink")
    root_list.geometry("230x150")
    root_list.title("Room Key")



    Label(root_list, text="Your room key is:- ", font="comicsans 20", bg="pink", fg="dark blue").grid(row=0, column=2)
    Label(root_list, text=room_key, font="comicsans 20", bg="pink", fg="dark blue").grid(row=1, column=2)

    with open("Hotel Check In List.txt", "a") as f:
        f.write(f"Room Number(Checked In) - {room_key}\n-----------------------------------------------------------------------------------\n")


    Button(root_list, text="Ok", font="comicsans 20", bg="pink", fg="dark blue", command=okbutton).grid(row=3, column=2)

    root_list.mainloop()    

"""
Taking FeedBack from user
"""
def feedback():
    global feedback_root
    feedback_root = Tk()
    feedback_root.geometry("404x330")
    feedback_root.title("Guest Status")
    feedback_root.config(bg="DeepSkyBlue2")

    Label(feedback_root, text="PLease give us you feedback:-", font="comicsans 20 bold", bg="purple").grid(row=0, column=0)
    Label(feedback_root, text="Other:-", font="comicsans 20 bold", bg="SpringGreen2").grid(row=5, column=0)
    
    global othervalue
    othervalue = StringVar()
    Entry(feedback_root, textvariable=othervalue, font="normal 20").grid(row=6, column=0)

    global var_feedback
    var_feedback = StringVar()
    var_feedback.set("FeedBack")

    feedback_option = Radiobutton(feedback_root, text="Excellent", variable = var_feedback, pady="5", font="normal 12", value="Excellent", bg="gold")
    feedback_option.grid(row=1, column=0)
    feedback_option = Radiobutton(feedback_root, text="Good", variable = var_feedback, pady="5", font="normal 12", value="Good", bg="gold")
    feedback_option.grid(row=2, column=0)
    feedback_option = Radiobutton(feedback_root, text="Need To Improve", variable = var_feedback, pady="5", font="normal 12", value="Need To Improve", bg="gold")
    feedback_option.grid(row=3, column=0)
    feedback_option = Radiobutton(feedback_root, text="Bad", variable = var_feedback, pady="5", font="normal 12", value="Bad", bg="gold")
    feedback_option.grid(row=4, column=0)

    Button(feedback_root, text="Submit", bg="Brown4", font="normal 15", command=feedbackbutton).grid(row=7, column=0)

    feedback_root.mainloop()

"""
Varifying Check-out Entry Using Chech-in Data
"""

def exitwindow():
    with open("G:\\Python-Manan\\Hotel Check In List.txt", "r") as f:
        readcontent = f.read()

        if name_outvalue.get() and aadhar_outvalue.get() and phone_outvalue.get() and room_outvalue.get() in readcontent:
            message.showinfo("Thankyou", "You have successfully checked out.Thankyou for coming our Hotel Please come Again Thankyou,\nPythonWithManan[Hotel Owner]")
            root_out.destroy()

            with open("Hotel Check Out List.txt", "a") as f:
                f.write(f"Name - {name_outvalue.get()}\nAadhar Number - {aadhar_outvalue.get()}\nPhone Number - {phone_outvalue.get()}\nRoom Number(Checked out) - {room_outvalue.get()}\n--------------------------------------------------------------\n")
        
            feedback()

        else:
            message.showerror("Invalid Information", "Sir/Maam you have submited invalid information\nplease recheck and submit valid information.\nPythonWithManan[Hotel Owner]")
            root_out.destroy()
            homepage()


"""
Check-Out Function
"""

def checkoutbutton():
    try:
        root_homepage.destroy()
    except Exception as error:
        pass

    global root_out
    root_out = Tk()
    root_out.geometry("580x310")
    root_out.title("Check Out")
    root_out.config(bg="light coral")

    # message.showinfo("Check Out", "Please enter the following\nDetails to check out.\nThankyou,\nPythonWithManan[Hotel Owner]")
    Label(root_out, text="Check Out:-", bg="light coral", fg="dark slate grey", font="algerian 30 bold").grid()
    Label(root_out, text="Name (Full Name)", fg="purple3", bg="light coral", font="classic 20 underline").grid(row=1, column=0)
    Label(root_out, text="Aadhar Number", fg="purple3", bg="light coral", font="classic 20 underline").grid(row=2, column=0)
    Label(root_out, text="Phone Number", fg="purple3", bg="light coral", font="classic 20 underline").grid(row=3, column=0)
    Label(root_out, text="Room Number", fg="purple3", bg="light coral", font="classic 20 underline").grid(row=4, column=0)

    global name_outvalue
    global aadhar_outvalue
    global phone_outvalue
    global room_outvalue
    name_outvalue = StringVar()
    aadhar_outvalue = StringVar()
    phone_outvalue = StringVar()
    room_outvalue = StringVar()

    nameentry = Entry(root_out, textvariable=name_outvalue, font="normal 20")
    roomkeyentry = Entry(root_out, textvariable=aadhar_outvalue, font="normal 20")
    phone_number_entry = Entry(root_out, textvariable=phone_outvalue, font="normal 20")
    room_number_entry = Entry(root_out, textvariable=room_outvalue, font="normal 20")
    nameentry.grid(row=1, column=2)
    roomkeyentry.grid(row=2, column=2)
    phone_number_entry.grid(row=3, column=2)
    room_number_entry.grid(row=4, column=2)

    Button(root_out, text="Check Out", bg="black", fg="white", pady="5", font="normal 15", command=exitwindow).grid(row=5, column=2)
    Button(root_out, text="Exit/Quit", bg="black", fg="white", pady="5", font="normal 15", command=exitcheck_out).grid(row=6, column=2)
    

"""
Guest List Function
"""

def GuestList():
    os.startfile('G:\\Python-Manan\\Guest List.txt')


def Gueststatus():
    root_homepage.destroy()
    global status_root
    status_root = Tk()
    status_root.geometry("308x360")
    status_root.title("Guest Status")
    status_root.config(bg="OliveDrab1")

    Label(status_root, text="Guest Status:-", font="comicsans 30 bold", bg="blue2").grid(row=0, column=0)
    Label(status_root, text="Room Number", font="comicsans 20 bold", bg="OliveDrab1", fg="OliveDrab1").grid(row=1, column=0)
    # Label(status_root, text="Room Number", font="comicsans 20 bold", bg="light blue", fg="light blue").grid(row=4, column=0)
    Label(status_root, text="||Enter Room Number||", font="comicsans 20 bold", bg="OliveDrab1", fg="IndianRed3").grid(row=2, column=0)
    Label(status_root, text="|||Enter User Name|||", font="comicsans 20 bold", bg="OliveDrab1", fg="IndianRed3").grid(row=5, column=0)
    
    statusvalue = StringVar()
    namestatusvalue = StringVar()
    Entry(status_root, textvariable=statusvalue, font="comicsans 20 bold").grid(row=3, column=0)
    Entry(status_root, textvariable=namestatusvalue, font="comicsans 20 bold").grid(row=6, column=0)
    
    """ 
    Function For Reading rather user is checked in or checked out.
    """

    def Gueststatus_button():
        with open("Hotel Check Out List.txt", "r") as f:
            filecontent = f.read()

        if f"Room Number(Checked out) - {statusvalue.get()}" and namestatusvalue.get() in filecontent:
            message.showinfo("User Checked out", f"User {namestatusvalue.get()} is already checked\nout from our hotel Thank you,\nPythonWithManan[Hotel Owner]")
            status_root.destroy()
            homepage()

        else:
            with open("Hotel Check In List.txt", "r") as ff:
                filecontent_b = ff.read()

            if f"Room Number(Checked In) - {statusvalue.get()}" and namestatusvalue.get() in filecontent_b:
                message.showinfo("User Checked In", f"User {namestatusvalue.get()} is currently checked-in\nThank you - PythonWithManan[Hotel Owner]")
                status_root.destroy()
                homepage()    

            else:
                message.showerror("Invalid Information", "The details which you have entered\nare wrong please recheck and submit again.\nPythonWithManan[Hotel Owner]")
                status_root.destroy()
                homepage()
    
    Button(status_root, text="Submit", font="comicsans 20 bold", bg="black", fg="white", command=Gueststatus_button).grid(row=8, column=0)
    Button(status_root, text="Exit", font="comicsans 20 bold", bg="black", fg="white", command=exitgueststatus).grid(row=9, column=0)
    
    status_root.mainloop()

homepage()