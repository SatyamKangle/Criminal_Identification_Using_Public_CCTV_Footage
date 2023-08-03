from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
from dbConnection import conn3
from dbConnection import delete
import os
import re
import mysql.connector as con
import numpy as np
import sqlite3
from tkinter import filedialog

import mysql.connector as con
import sys
import mysql
import tkinter.messagebox
global var
from dbConnection import view_all_attendance
from dbConnection import conn5


import TrainModule
import FaceRecognation
global screen1

def main_screen():
    global screen1
    global filename

    screen1 = Tk()
    screen1.geometry("720x500")

    C = Canvas(screen1,height=250,width=300)
    filename = ImageTk.PhotoImage(Image.open('186040.gif'))
    background_label=Label(screen1,image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.create_image(0, 0, anchor=NW, image=filename)
    C.pack()

    #screen1.geometry("720x500")
    screen1.title("DASHBOARD")

    filename.image2 = ImageTk.PhotoImage(Image.open('186040.gif'))
    w = filename.image2.width()
    h = filename.image2.height()
    screen1.geometry('%dx%d+0+0' % (w, h))
    Label(screen1, text="Smart CCTV Surveillance for Criminal Detection", bg="Gray", height=2, width=250,
          font=("Arial Bold", 24)).pack()

    tool_bar = Frame(width=50, height=185, bg='lightgrey')
    tool_bar.pack(side='left', fill='both', padx=1, pady=1, expand=True)

    filter_bar = Frame(width=50, height=185, bg='lightgrey')
    filter_bar.pack(side='right', fill='both', padx=1, pady=1, expand=True)

    b1 = Button(tool_bar, text="Add police Station", height=2, width=50, bg="Black", fg="blue", font=("Arial Bold", 15),
                command=add_police_station)
    b1.pack(padx=5, pady=5)

    b2 = Button(tool_bar, text="View Police Station", height=2, width=50, bg="Black", fg="yellow",
                font=("Arial Bold", 15), command=view_police1)
    b2.pack(padx=5, pady=5)

    b3 = Button(tool_bar, text="Add Criminal Record", height=2, width=50, bg="black", fg="blue",
                font=("Arial Bold", 15), command=add_criminal)
    b3.pack(padx=5, pady=5)

    b4 = Button(filter_bar, text="Train Model", height=2, width=50, bg="black", fg="red", font=("Arial Bold", 15),
                command=train_model)
    b4.pack(padx=5, pady=5)

    b5 = Button(filter_bar, text="Live Camera Feeding", height=2, width=50, bg="black", fg="yellow",
                font=("Arial Bold", 15), command=mark_attnd)
    b5.pack(padx=5, pady=5)

    b6 = Button(filter_bar, text="Exit", height=2, width=50, bg="black", fg="blue", font=("Arial Bold", 15),
                command=screen1.destroy)
    b6.pack(padx=5, pady=5)

    #C = Canvas(screen1)
    #filename = ImageTk.PhotoImage(Image.open('186040.gif'))
    #background_label = Label(screen1, image=filename)
    #C.pack()

    b7 = Button(screen1, text="Exit", height=2, width=50, bg="Black", fg="green", font=("Arial Bold", 15),
                command=screen1.destroy)
    b7.pack()

    screen1.mainloop()


def add_police_station():

    global new_screen3
    global head_name_log
    global address_log
    global lat__log
    global long__log
    global email_log
    global mobile_log

    new_screen3 =Toplevel(screen1)
    new_screen3.configure(background='white')
    new_screen3.geometry('1280x720')

    Label(new_screen3, text="Add Police Station", font=("Arial Bold", 25), bg="grey", width=250, height=2).pack()
    Label(new_screen3, text="", bg="white").pack()
    Label(new_screen3, text="", bg="white").pack()

    head_name = Label(new_screen3, text="Head Name", fg="Blue", height=2, font=("Arial Bold", 11))
    head_name.pack()
    head_name_log = Entry(new_screen3, width=60)
    head_name_log.pack()

    address = Label(new_screen3, text="Address", fg="Blue", height=2, font=("Arial Bold", 11))
    address.pack()
    address_log = Entry(new_screen3, width=60)
    address_log.pack()

    lat_ = Label(new_screen3, text="Latitude", fg="Blue", height=2, font=("Arial Bold", 11))
    lat_.pack()
    lat__log = Entry(new_screen3, width=60)
    lat__log.pack()

    long_ = Label(new_screen3, text="Longitude", fg="Blue", height=2, font=("Arial Bold", 11))
    long_.pack()
    long__log = Entry(new_screen3, width=60)
    long__log.pack()

    email = Label(new_screen3, text="Email", fg="Blue", height=2, font=("Arial Bold", 11))
    email.pack()
    email_log = Entry(new_screen3, width=60)
    email_log.pack()

    mobile = Label(new_screen3, text="Mobile", fg="Blue", height=2, font=("Arial Bold", 11))
    mobile.pack()
    mobile_log = Entry(new_screen3, width=60)
    mobile_log.pack()

    Label(new_screen3, text="", bg="white").pack()
    Label(new_screen3, text="", bg="white").pack()

    add = Button(new_screen3, text="Add", height=2, width=30, command=add_police_record, bg="Blue", fg="white",
                 font=("Arial Bold", 13))
    add.pack()

    back_button = Button(new_screen3, text="Back", height=1, width=20, bg="black", fg="Red", font=("Arial Bold", 10),
                         command=new_screen3.destroy)
    back_button.pack()

from dbConnection import conn
import dbConnection

def add_police_record():
    db = con.connect(host="localhost", port=3307, user="root", password='', database="db_accident")
    cur = db.cursor()

    head_name = head_name_log.get()
    address = address_log.get()
    lat_ = lat__log.get()
    long_ = long__log.get()
    email = email_log.get()
    mobile = mobile_log.get()

    query = "INSERT INTO `tbl_police`(`head_name`, `address`, `lat_`, `long_`, `email`, `mobile`)VALUES(%s,%s,%s,%s,%s,%s)"
    value = [head_name, address, lat_, long_, email, mobile]


    if (not (check(email))):
        messagebox.showinfo("Information", "Email wrong")
    elif (not (isValid(mobile))):
        messagebox.showinfo("Information", "Mobile wrong")
    elif len(head_name) == 0:
        messagebox.showinfo("Information", "Empty Head nane")
    elif len(address) == 0:
        messagebox.showinfo("Information", "Empty Address")
    elif len(lat_) == 0:
        messagebox.showinfo("Information", "Empt Latitude")
    elif len(long_) == 0:
        messagebox.showinfo("Information", "Empty Longitude")
    elif len(email) == 0:
        messagebox.showinfo("Information", "Empty Email")
    elif len(mobile) == 0:
        messagebox.showinfo("Information", "Empty Mobile")
    else:
        cur.execute(query, value)
        db.commit()
        messagebox.showinfo("Information", "Details Added Successfully.")

def view_police1():
    global window
    global screen1

    # Create the main window
    def view_police():

        global window
        global screen1

        window = Toplevel(screen1)
        window.title("View Police Station")
        window.geometry('920x520')

        # Add a canvas with a background image
        C = Canvas(window, height=180, width=720)
        filename = ImageTk.PhotoImage(Image.open('186040.gif'))
        background_label = Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.create_image(0, 0, anchor=NW, image=filename)
        C.pack()

        # Create a treeview widget to display the police station details
        tree = ttk.Treeview(window)
        tree["column"] = ("ID", "Police Station Name", "Address", "Latitude", "Longitude", "Email", "Mobile No")
        tree.column("ID", width=50)
        tree.heading("ID", text="ID")
        tree.column("Police Station Name", width=150)
        tree.heading("Police Station Name", text="Police Station Head Name")
        tree.column("Address", width=100)
        tree.heading("Address", text="Address")
        tree.column("Latitude", width=100)
        tree.heading("Latitude", text="Latitude")
        tree.column("Longitude", width=100)
        tree.heading("Longitude", text="Longitude")
        tree.column("Email", width=100)
        tree.heading("Email", text="Email")
        tree.column("Mobile No", width=100)
        tree.heading("Mobile No", text="Mobile No")
        tree.bind('<ButtonRelease-1>', lambda event: selectItem(tree))

        # Retrieve the police station details from the database and insert them into the treeview widget
        db = con.connect(host="localhost", port=3307, user="root", password='', database="db_accident")
        cur = db.cursor()
        cur.execute("SELECT * FROM tbl_police")
        row = cur.fetchall()

        cpt = 0
        for i in row:
            tree.insert('', 'end', values=i)
            cpt += 1

        tree.pack()

        # Add a button to go back to the previous screen
        back_button = Button(window, text="Back", height=1, width=20, bg="Black", fg="red", font=("Arial Bold", 10),
                             command=window.destroy)
        back_button.pack()

        # Add a label to indicate how to delete a row
        Label(window, text="Click on a data to delete", bg="Black", fg="red", height=1, width=250,
              font=("Arial Bold", 12)).pack()

        window.mainloop()

    # Define a function to delete a row from the database when it is selected in the treeview widget
    def selectItem(tree):
        curItem = tree.focus()
        head_name = tree.item(curItem)
        print(head_name)
        x = head_name["values"]
        print(x)
        y = x[0]

        delete(y)
        window.destroy()
        window.after(1000, view_police)

    # Start the main event loop

    view_police()

import TrainModule
def train_model():
    TrainModule.train1()

def add_criminal():
    global new_screen5
    global name
    global mobile
    global address
    global div_
    global adh_
    global em_
    global variable

    new_screen5 = Toplevel(screen1)
    new_screen5.configure(background='white')
    new_screen5.geometry('1280x720')

    Label(new_screen5, text="Criminal Identification", font=("Arial Bold", 25), bg="grey", width=250, height=2).pack()
    Label(new_screen5, text="", bg="white").pack()
    Label(new_screen5, text="", bg="white").pack()

    name = Label(new_screen5, text="Name", height=2, bg="white", font=("Arial Bold", 11))
    name.pack()
    name = Entry(new_screen5, width=60)
    name.pack()

    mobile = Label(new_screen5, text="mobile", height=2, bg="white", font=("Arial Bold", 11))
    mobile.pack()
    mobile = Entry(new_screen5, width=60)
    mobile.pack()

    address = Label(new_screen5, text="Address", height=2, bg="white", font=("Arial Bold", 11))
    address.pack()
    address = Entry(new_screen5, width=60)
    address.pack()

    div_ = Label(new_screen5, text="Crimes", height=2, bg="white", font=("Arial Bold", 11))
    div_.pack()
    div_ = Entry(new_screen5, width=60)
    div_.pack()

    adh_ = Label(new_screen5, text="Adhar Number", height=2, bg="white", font=("Arial Bold", 11))
    adh_.pack()
    adh_ = Entry(new_screen5, width=60)
    adh_.pack()

    em_ = Label(new_screen5, text="Email", height=2, bg="white", font=("Arial Bold", 11))
    em_.pack()
    em_ = Entry(new_screen5, width=60)
    em_.pack()



    OPTIONS = [
        "Select Criminal Type",
        "Green",
        "Yellow",
        "Red"
    ]

    variable = StringVar(new_screen5)
    variable.set(OPTIONS[0])  # default value

    w = OptionMenu(new_screen5, variable, *OPTIONS)
    w.pack()

    Label(new_screen5, text="", bg="white").pack()
    Label(new_screen5, text="", bg="white").pack()

    login = Button(new_screen5, text="Add Record", height=2, width=30, command=record_faces, bg="black", fg="white",
    font=("Arial Bold", 13))
    login.pack()

    back_button = Button(new_screen5, text="Back", height=1, width=20, bg="black", fg="Red", font=("Arial Bold", 10),
                         command=new_screen5.destroy)
    back_button.pack()

def record_faces():

    a = name.get()
    b = mobile.get()
    c = div_.get()
    d = address.get()
    e = adh_.get()
    f = em_.get()
    g = variable.get()

    print(a)
    path1 = 'dataset'
    model_detector = 'opencv_face_detector.pbtxt'
    imagePaths = [os.path.join(path1, f) for f in os.listdir(path1)]
    print(imagePaths)

    id = 1;
    for imagePath in imagePaths:

        print(os.path.split(imagePath)[-1].split('.')[2])

        ID = int(os.path.split(imagePath)[-1].split('.')[2])
        if ID > id:
            id = ID
    if not os.path.exists('./dataset'):
        os.makedirs('./dataset')
    # c = conn.cursor()
    face_cascade = cv2.CascadeClassifier('haar.xml')
    cap = cv2.VideoCapture(0)
    # uname = input("Enter your name: ")

    sampleNum = id + 20

    if (not (check(f))):
        messagebox.showinfo("Information", "Email wrong")

    elif (not (isValid(b))):
        messagebox.showinfo("Information", "Mobile wrong")

    elif (not (isValidAadhaarNumber(e))):
        messagebox.showinfo("Information", "Adhar Number wrong")
    elif len(a) == 0:
        messagebox.showinfo("Information", "Empty Name")
    elif len(b) == 0:
        messagebox.showinfo("Information", "Empty Mobile")
    elif len(c) == 0:
        messagebox.showinfo("Information", "Empty Crime details")
    elif len(d) == 0:
        messagebox.showinfo("Information", "Empty Address")
    elif len(e) == 0:
        messagebox.showinfo("Information", "Empty Adhar Number")
    elif len(f) == 0:
        messagebox.showinfo("Information", "Empty Email")

    else:
        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                id = id + 1
                cv2.imwrite("dataset/User." + str(a) + "." + str(id) + ".jpg", gray[y:y + h, x:x + w])
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.waitKey(100)
                conn5(id, a, b, d, c, e, f, g)
            cv2.imshow('img', img)
            cv2.waitKey(1);
            if id > sampleNum:
                break
        cap.release()
        messagebox.showinfo("Information", "Criminal Record Added Successfully.")

    # conn.commit()
    # conn.close()
    cv2.destroyAllWindows()

def mark_attnd():
    FaceRecognation.mark_attend()

def isValid(s):

    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(s)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False


def isValidAadhaarNumber(str):
    regex = ("^[2-9]{1}[0-9]{3}\\" +
             "s[0-9]{4}\\s[0-9]{4}$")
    p = re.compile(regex)
    if (str == None):
        return False
    if (re.search(p, str)):
        return True
    else:
        return False

def backandclose():
    os.system('python dashboard.py')
    screen1.destroy()
    screen1.quit()

main_screen()




