"""
Function of Buttons
"""
############################
### ADD STUDENT FUNCTION ###
############################

def addstudent():
    """
    Submit Button Function
    """ 

    def submitadd():
        global mycursor
        global con

        id = idvar.get()
        name = namevar.get()
        mobile = mobilevar.get()
        email = emailvar.get()
        address = addressvar.get()
        gender = gendervar.get()
        dob = dobvar.get()
        addedtime = time.strftime("%I:%M:%S-%p")
        addeddate = time.strftime("%d/%m/%Y")    
        try:
            strr = 'INSERT INTO studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            val = (id, name, mobile, email, address, gender, dob, addeddate, addedtime)
            mycursor.execute(strr, val)
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions', 'Id {} Name {} Added sucessfully.. and do you want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idvar.set('')
                namevar.set('')
                mobilevar.set('')
                emailvar.set('')
                addressvar.set('')
                gendervar.set('Choose Gender')
                dobvar.set('')
            else:
                pass    
        except:
            messagebox.showerror('Invalid ID or database', 'ID already exit try another ID Or\nMay be you are not connected to database.', parent=addroot)
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        data = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    addroot = Toplevel(master=DateEntryFrame)
    addroot.grab_set()
    addroot.geometry('390x410+212+110')
    addroot.title('Add Sudent')
    addroot.iconbitmap('icon.ico')
    addroot.config(bg='DodgerBlue4')
    addroot.resizable(False, False)

    """
    Add Student Lables and Entries
    """
    idlable = Label(addroot, text='Enter ID :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlable.place(x=8, y=8)

    Namelable = Label(addroot, text='Enter Name :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Namelable.place(x=8, y=58)

    Mobilelable = Label(addroot, text='Enter Mobile :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Mobilelable.place(x=8, y=108)

    Emaillable = Label(addroot, text='Enter Email :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Emaillable.place(x=8, y=158)

    Addresslable = Label(addroot, text='Enter Address :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Addresslable.place(x=8, y=208)

    Genderlable = Label(addroot, text='Enter Gender :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Genderlable.place(x=8, y=258)
    
    doblable = Label(addroot, text='Enter D.O.B :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    doblable.place(x=8, y=308)

    """
    Add Student Entries
    """
    #Variables
    idvar = StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    emailvar = StringVar()
    addressvar = StringVar()
    gendervar = StringVar()
    gendervar.set('')
    dobvar = StringVar()
    dobvar.set('')

    identry = Entry(addroot, font='times 12 bold', borderwidth=4, textvariable=idvar)
    identry.place(x=210, y=8)

    nameentry = Entry(addroot, font='times 12 bold', borderwidth=4, textvariable=namevar)
    nameentry.place(x=210, y=58)

    moblieentry = Entry(addroot, font='times 12 bold', borderwidth=4, textvariable=mobilevar)
    moblieentry.place(x=210, y=108)

    emailentry = Entry(addroot, font='times 12 bold', borderwidth=4, textvariable=emailvar)
    emailentry.place(x=210, y=158)

    addressentry = Entry(addroot, font='times 12 bold', borderwidth=4, textvariable=addressvar)
    addressentry.place(x=210, y=208)

    genderentry = OptionMenu(addroot, gendervar,'Male', 'Female', 'Other')
    genderentry.place(x=210, y=258)

    dobentry = DateEntry(addroot, font='times 12 bold', borderwidth=4, textvariable=dobvar)
    dobentry.place(x=210, y=308)

    #Button For Submit
    submitbtn = Button(addroot, text='Submit', font='Times 12 bold', width=17, borderwidth=4, bg='red',command=submitadd)
    submitbtn.place(x=115, y=360)

    addroot.mainloop()

###############################
### SEARCH STUDENT FUNCTION ###
###############################

def searchstudent():
    """
    Submit Button Function
    """

    def submitsearch():
        id = idvar.get()
        name = namevar.get()
        mobile = mobilevar.get()
        email = emailvar.get()
        address = addressvar.get()
        gender = gendervar.get()
        dob = dobvar.get()
        addeddate = time.strftime("%d/%m/%Y")

        if(id != ''):
            strr = 'select *from studentdata where id=%s'
            mycursor.execute(strr, (id))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(name != ''):
            strr = 'select *from studentdata where name=%s'
            mycursor.execute(strr, (name))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
                
        elif(mobile != ''):
            strr = 'select *from studentdata where mobile=%s'
            mycursor.execute(strr, (mobile))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(email != ''):
            strr = 'select *from studentdata where email=%s'
            mycursor.execute(strr, (email))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(address != ''):
            strr = 'select *from studentdata where address=%s'
            mycursor.execute(strr, (address))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(gender != ''):
            strr = 'select *from studentdata where gender=%s'
            mycursor.execute(strr, (gender))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(dob != ''):
            strr = 'select *from studentdata where dob=%s'
            mycursor.execute(strr, (dob))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select *from studentdata where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            data = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DateEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('390x460+212+110')
    searchroot.title('Search Sudent')
    searchroot.iconbitmap('icon.ico')
    searchroot.config(bg='tomato')
    searchroot.resizable(False, False)

    """
    Add Student Lables and Entries
    """
    idlable = Label(searchroot, text='Search By ID :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=16, anchor='w')
    idlable.place(x=8, y=8)

    Namelable = Label(searchroot, text='Search By Name :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=16, anchor='w')
    Namelable.place(x=8, y=58)

    Mobilelable = Label(searchroot, text='Search By Mobile :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=16, anchor='w')
    Mobilelable.place(x=8, y=108)

    Emaillable = Label(searchroot, text='Search By Email :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=16, anchor='w')
    Emaillable.place(x=8, y=158)

    Addresslable = Label(searchroot, text='Search By Address :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=16, anchor='w')
    Addresslable.place(x=8, y=208)

    Genderlable = Label(searchroot, text='Search By Gender :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=16, anchor='w')
    Genderlable.place(x=8, y=258)
    
    doblable = Label(searchroot, text='Search By D.O.B :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=16, anchor='w')
    doblable.place(x=8, y=308)

    datelable = Label(searchroot, text='Search By Date :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=16, anchor='w')
    datelable.place(x=8, y=348)

    """
    Search Student Entries
    """
    #Variables
    idvar = StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    emailvar = StringVar()
    addressvar = StringVar()
    gendervar = StringVar()
    gendervar.set('')
    dobvar = StringVar()
    datevar = StringVar()

    identry = Entry(searchroot, font='times 10 bold', borderwidth=4, textvariable=idvar)
    identry.place(x=230, y=8)

    nameentry = Entry(searchroot, font='times 10 bold', borderwidth=4, textvariable=namevar)
    nameentry.place(x=230, y=58)

    moblieentry = Entry(searchroot, font='times 10 bold', borderwidth=4, textvariable=mobilevar)
    moblieentry.place(x=230, y=108)

    emailentry = Entry(searchroot, font='times 10 bold', borderwidth=4, textvariable=emailvar)
    emailentry.place(x=230, y=158)

    addressentry = Entry(searchroot, font='times 10 bold', borderwidth=4, textvariable=addressvar)
    addressentry.place(x=230, y=208)

    genderentry = OptionMenu(searchroot, gendervar,'Male', 'Female', 'Other')
    genderentry.place(x=230, y=258)

    dobentry = DateEntry(searchroot, font='times 10 bold', borderwidth=4, textvariable=dobvar)
    dobentry.place(x=230, y=308)
    dobvar.set('')

    dateentry = DateEntry(searchroot, font='times 10 bold', borderwidth=4, textvariable=datevar)
    dateentry.place(x=230, y=358)
    datevar.set('')

    #Button For Submit
    submitbtn = Button(searchroot, text='Search Student', font='Times 12 bold', width=17, borderwidth=4, bg='DodgerBlue4',command=submitsearch)
    submitbtn.place(x=115, y=405)

    searchroot.mainloop()

###############################
### DELETE STUDENT FUNCTION ###
###############################
def deletestudent():
    try:
        cc = studenttable.focus()
        content = studenttable.item(cc)
        pp = content['values'][0]
        strr = 'delete from studentdata where id=%s'
        mycursor.execute(strr,(pp))
        con.commit()
        messagebox.showinfo('Deleted','Id {} deleted sucessfully...'.format(pp))
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)
    except:
        messagebox.showerror('Error', 'First connect to database,\nThen select one student then delete.')
###############################
### UPDATE STUDENT FUNCTION ###
###############################
"""
def updatestudent():

    Submit Button Function

    def submitupdate():
        id = idvar.get()
        name = namevar.get()
        mobile = mobilevar.get()
        email = emailvar.get()
        address = addressvar.get()
        gender = gendervar.get()
        dob = dobvar.get()
        timee = timevar.get()
        date = datevar.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,timee,id))
        con.commit()
        messagebox.showinfo('Updated', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        data = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DateEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('390x510+212+110')
    updateroot.title('Search Sudent')
    updateroot.iconbitmap('icon.ico')
    updateroot.config(bg='SeaGreen3')
    updateroot.resizable(False, False)

    Update Student Lables

    idlable = Label(updateroot, text='Update ID :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlable.place(x=8, y=8)

    Namelable = Label(updateroot, text='Update Name :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Namelable.place(x=8, y=58)

    Mobilelable = Label(updateroot, text='Update Mobile :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Mobilelable.place(x=8, y=108)

    Emaillable = Label(updateroot, text='Update Email :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Emaillable.place(x=8, y=158)

    Addresslable = Label(updateroot, text='Update Address :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Addresslable.place(x=8, y=208)

    Genderlable = Label(updateroot, text='Update Gender :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    Genderlable.place(x=8, y=258)
    
    doblable = Label(updateroot, text='Update D.O.B :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    doblable.place(x=8, y=308)

    datelable = Label(updateroot, text='Update Date :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelable.place(x=8, y=358)

    timelable = Label(updateroot, text='Update Time :', bg='gold2', font='Helvatica 16 bold', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    timelable.place(x=8, y=408)

    Update Student Entries

    #Variables
    idvar = StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    emailvar = StringVar()
    addressvar = StringVar()
    gendervar = StringVar()
    gendervar.set('Choose Gender')
    dobvar = StringVar()
    datevar = StringVar
    timevar = StringVar()

    identry = Entry(updateroot, font='times 12 bold', borderwidth=4, textvariable=idvar)
    identry.place(x=210, y=8)

    nameentry = Entry(updateroot, font='times 12 bold', borderwidth=4, textvariable=namevar)
    nameentry.place(x=210, y=58)

    moblieentry = Entry(updateroot, font='times 12 bold', borderwidth=4, textvariable=mobilevar)
    moblieentry.place(x=210, y=108)

    emailentry = Entry(updateroot, font='times 12 bold', borderwidth=4, textvariable=emailvar)
    emailentry.place(x=210, y=158)

    addressentry = Entry(updateroot, font='times 12 bold', borderwidth=4, textvariable=addressvar)
    addressentry.place(x=210, y=208)

    genderentry = OptionMenu(updateroot, gendervar,'Male', 'Female', 'Other')
    genderentry.place(x=210, y=258)

    dobentry = DateEntry(updateroot, font='times 12 bold', borderwidth=4, textvariable=dobvar)
    dobentry.place(x=210, y=308)
    dobvar.set('Choose D.O.B')

    dateentry = DateEntry(updateroot, font='times 12 bold', borderwidth=4, textvariable=datevar)
    dateentry.place(x=210, y=358)
    
    timeentry = Entry(updateroot, font='times 12 bold', borderwidth=4, textvariable=timevar)
    timeentry.place(x=210, y=408)

    #Button For Submit
    submitbtn = Button(updateroot, text='Update', font='Times 12 bold', width=17, borderwidth=4, bg='FireBrick2',command=submitupdate)
    submitbtn.place(x=115, y=455)

    cc = studenttable.focus()
    contect = studenttable.item(cc)
    pp = contect['values']
    if(len(pp) !=0):
        idvar.set(pp[0])
        namevar.set(pp[1])
        mobilevar.set(pp[2])
        emailvar.set(pp[3])
        addressvar.set(pp[4])
        gendervar.set(pp[5])
        dobvar.set(pp[6])
        # datevar.set('')
        timevar.set(pp[8])

    updateroot.mainloop()
"""

#################################
### Show ALl STUDENT FUNCTION ###
#################################
def allstudent():
    try:
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)
    except:
        messagebox.showerror('Notification', 'Database not found first connect to it.')        

###############################
### EXPORT STUDENT FUNCTION ###
###############################
def exportdata():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0])
        name.append(pp[1])
        mobile.append(pp[2])
        email.append(pp[3])
        address.append(pp[4])
        gender.append(pp[5]),
        dob.append(pp[6])
        addeddate.append(pp[7])
        addedtime.append(pp[8])

    """
    Giving heading to our file.
    """    
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']

    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)), columns=dd)

    """
    Saving Our content
    """

    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Data Saved', 'Student data is Saved.\nLocation - {}'.format(paths))

#############################
### EXIT STUDENT FUNCTION ###
#############################
def exitstudent():
    res = messagebox.askyesnocancel('Confirm Exit', 'Are you Sure, You want to exit?')
    if res == True:
        root.destroy()
    else:
        pass

"""
Imports
"""
from tkinter import *
import time
import random
from tkinter import Toplevel, filedialog
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.ttk import Treeview
import pymysql
import pandas


"""
Functions
"""

def Connectdb():
    
    """
    Function WHich will connect you to database
    """

    def submitdb():
        global con, mycursor
        host = hostvar.get()
        user = uservar.get()
        password = passwordvar.get()
        # host = 'localhost'
        # user = 'PythonWithManan'
        # password = 'pythonwithmanan'

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Wrong Data', 'Your Data is incorrect\nPlease Try Again.')
            dbroot.destroy()
            Connectdb()

        try:
            strr = 'create database studentmanagementsystem;'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem;'
            mycursor.execute(strr)
            strr = 'CREATE TABLE studentdata(id INT(11) NOT NULL PRIMARY KEY, name VARCHAR(25), mobile VARCHAR(12), email VARCHAR(30),address VARCHAR(120), gender VARCHAR(50), dob VARCHAR(20), date VARCHAR(20), time VARCHAR(20));'
            mycursor.execute(strr)
            messagebox.showinfo('Conected To Database', 'Your Database is Created and connected\nwith us.')
            dbroot.destroy()
        except:
            strr = 'use studentmanagementsystem;'
            mycursor.execute(strr)
            messagebox.showinfo('Conected To Database', 'Now You are connected to the Database.')
            dbroot.destroy()



    dbroot = Toplevel()
    dbroot.iconbitmap('icon.ico')
    dbroot.grab_set()
    dbroot.title('Connect to DataBase - PythonWIthManan')
    dbroot.geometry('400x250+707+210')
    dbroot.iconbitmap('icon.ico')
    dbroot.resizable(False, False)
    dbroot.configure(bg='Royal Blue')
    """
    ConnectDB Labels
    """
    hostlable = Label(dbroot, text="Enter Host :", bg='gold2', font='times 15 bold', relief=GROOVE, borderwidth=3, width=13, anchor='w')
    hostlable.place(x=8, y=10)


    userlable = Label(dbroot, text="Enter User :", bg='gold2', font='times 15 bold', relief=GROOVE, borderwidth=3, width=13, anchor='w')
    userlable.place(x=8, y=63)


    passwordlable = Label(dbroot, text="Enter Password :", bg='gold2', font='times 15 bold', relief=GROOVE, borderwidth=3, width=13, anchor='w')
    passwordlable.place(x=8, y=117)

    """
    ConnectDB Entries
    """
    #########--Entry Variables--#########
    hostvar = StringVar()
    uservar = StringVar()
    passwordvar = StringVar()
    
    hostentry = Entry(dbroot, font='times 15 bold', borderwidth=4, width=18, textvariable=hostvar)
    hostentry.place(x=197, y=10)

    userentry = Entry(dbroot, font='times 15 bold', borderwidth=4, width=18, textvariable=uservar)
    userentry.place(x=197, y=63)

    passwordentry = Entry(dbroot, font='times 15 bold', borderwidth=4, width=18, textvariable=passwordvar, show='*')
    passwordentry.place(x=197, y=117)


    #################################
    ### Show/Hide Button Function ###
    #################################
    def showpassword():
        passwordentry = Entry(dbroot, font='times 15 bold', borderwidth=4, width=18, textvariable=passwordvar, show='')
        passwordentry.place(x=197, y=117)

    def hidepassword():
        passwordentry = Entry(dbroot, font='times 15 bold', borderwidth=4, width=18, textvariable=passwordvar, show='*')
        passwordentry.place(x=197, y=117)  

    """
    Button for connecting DataBase
    """
    submitbutton = Button(dbroot, text="Connect", font='chillar 13 bold', width=17, bg='Orange Red2', borderwidth=7, command=submitdb)
    submitbutton.place(x=114, y=200)

    showbtn = Button(dbroot, text="Show", font='chillar 8 bold', width=8, bg='green', borderwidth=7, command=showpassword)
    showbtn.place(x=310, y=152)

    hidebtn = Button(dbroot, text="Hide", font='chillar 8 bold', width=8, bg='red', borderwidth=7, command=hidepassword)
    hidebtn.place(x=234, y=152)

    dbroot.mainloop()


def IntroLableColorTick():
    colors = ['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'purple3']
    fg = random.choice(colors)
    SliderLable.config(fg=fg)
    SliderLable.after(20, IntroLableColorTick)

def tick():
    time_string = time.strftime('%I:%M:%S-%p')
    date_string = time.strftime('---%d/%m/%y---')
    clock.config(text="Date : "+date_string+"\nTime : "+time_string)
    clock.after(200, tick)

def IntroLableTick():
    global count, text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLable.configure(text=text)

    else:
        text = text + ss[count]
        SliderLable.configure(text=text)    
        count += 1

    SliderLable.after(170, IntroLableTick)     

"""
Configuring Root
"""
root = Tk()
root.title('StudentManagementSystem - PythonWithManan')
root.configure(bg='gold2')
root.geometry('1000x600+183+50')
root.iconbitmap('icon.ico')
root.resizable(False, False)

"""
Creating Frames (Main Window)
"""

DateEntryFrame = Frame(root, bg='chocolate2', relief=GROOVE, borderwidth=5)
DateEntryFrame.place(x=10, y=80, width=430, height=500)

"""
#######--Making buttons and lable in Data Entry Frame--######
"""
frontlable = Label(DateEntryFrame, text='------------------Welcome------------------', width=26, font='arial 18 bold', bg='chocolate2')
frontlable.pack(side=TOP, expand=True)

#Add Button
addbtn = Button(DateEntryFrame, text='1. Add Student', width=19, font='Helvatica 15 bold', borderwidth=6, bg='purple2', relief=RIDGE, command=addstudent)
addbtn.pack(side=TOP, expand=True)

#Sreach Student
searchbtn = Button(DateEntryFrame, text='2. Search Student', width=19, font='Helvatica 15 bold', borderwidth=6, bg='purple2', relief=RIDGE, command=searchstudent)
searchbtn.pack(side=TOP, expand=True)

#Delete Student
deletebtn = Button(DateEntryFrame, text='3. Delete Student', width=19, font='Helvatica 15 bold', borderwidth=6, bg='purple2', relief=RIDGE, command=deletestudent)
deletebtn.pack(side=TOP, expand=True)

#Update Student
# updatebtn = Button(DateEntryFrame, text='4. Update Student', width=19, font='Helvatica 15 bold', borderwidth=6, bg='purple2', relief=RIDGE, command=updatestudent)
# updatebtn.pack(side=TOP, expand=True)

#Show All
allbtn = Button(DateEntryFrame, text='5. All Students', width=19, font='Helvatica 15 bold', borderwidth=6, bg='purple2', relief=RIDGE, command=allstudent)
allbtn.pack(side=TOP, expand=True)

#Export Data
exportbtn = Button(DateEntryFrame, text='6. Export Data', width=19, font='Helvatica 15 bold', borderwidth=6, bg='purple2', relief=RIDGE, command=exportdata)
exportbtn.pack(side=TOP, expand=True)

#Student Exit
exitbtn = Button(DateEntryFrame, text='7. Exit', width=19, font='Helvatica 15 bold', borderwidth=6, bg='purple2', relief=RIDGE, command=exitstudent)
exitbtn.pack(side=TOP, expand=True)

mylable = Label(DateEntryFrame, text='Devoloped By - PythonWithManan', font='Helvatica 18 bold', borderwidth=6, bg='red', relief=RIDGE)
mylable.pack(side=TOP, expand=True)
#--------------------------------------------------------------------------------------------------------------#

ShowDataFrame = Frame(root, bg='chocolate2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=450, y=80, width=540, height=500)

"""
Making Show Data Frame and connecting to Database
"""
style = ttk.Style()
style.configure('Treeview.Heading', font='Helvetica 13 bold', foreground='blue2')

style.configure('Treeview', font='times 13 bold', background="black", 
foreground="white", fieldbackground="black")

### Making Scroll Bar ###
Scrolbar_X = Scrollbar(ShowDataFrame,  orient=HORIZONTAL)
Scrolbar_X.pack(side=BOTTOM, fill=X)
Scrolbar_Y = Scrollbar(ShowDataFrame,  orient='vertical')
Scrolbar_Y.pack(side=RIGHT, fill=Y)

studenttable = Treeview(ShowDataFrame, columns=('ID', 'Student Name', 'Mobile Number', 'Email Address', 'Address',  'Gender', 'Date Of Birth', 'Added Date', 'Added Time'), yscrollcommand=Scrolbar_Y.set, xscrollcommand=Scrolbar_X.set)
studenttable.pack(fill=BOTH, expand=1)

### Configuring Scroll Bars ###
Scrolbar_X.config(command=studenttable.xview)
Scrolbar_Y.config(command=studenttable.yview)

### Writing Heading to Colunm
studenttable.heading('ID', text='ID')
studenttable.heading('Student Name', text='Student Name')
studenttable.heading('Mobile Number', text='Mobile Number')
studenttable.heading('Email Address', text='Email Address')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('Date Of Birth', text='Date Of Birth')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time') 
#SHowing only heading.
studenttable['show'] = 'headings'

"""
Slider(Top Window)
"""
##########Color Changing##########
colors = ['red', 'green', 'blue', 'yellow']
print()

ss = 'Welcome To Student Management System'
count = 0
text = ''

SliderLable = Label(root, text=ss, font=('chiller', 25, 'italic bold'), relief=RIDGE, borderwidth=5, width=39, bg='cyan')
SliderLable.place(x=230, y=0)
IntroLableTick()
IntroLableColorTick()

############**********Clock**********############
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=5, bg='lawn green')
clock.place(x=0, y=0)
tick()

"""
Connect to DataBase (Button)
"""
connectbutton = Button(root, text='Connect To Database', width=16, font=('times', 16, 'italic bold'), relief=RIDGE, borderwidth=5, bg='lawn green', activebackground='green', activeforeground='white', command=Connectdb)
connectbutton.place(x=792, y=0)

root.mainloop()