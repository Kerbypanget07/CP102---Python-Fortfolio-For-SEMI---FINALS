import time
import re
import hashlib
import datetime
import mysql.connector
import tkinter as tk
from tkinter import *

def ld():
    c = "Now Loading"
    print(c, end="")
    for a in "...":
        time.sleep(0.5)
        print(a, end="")
    print()

def wlc():
    for d in "\nGreetings, Welcome to Kear's Restaurant! ver 1.0":
        time.sleep(0.1)
        print(d, end="")
    print()

def pgm(answer):
    if answer.lower() == "y":
        return "Welcome!"
    elif answer.lower() == "n":
        return "Goodbye."
    else:
        return "Please input Y or N only."

print ()

ld()
time.sleep(1)
wlc()

while True:
    v = "\nWould you like to launch the program? (Y/N)"
    print(v)
    try:
        answer = input("Response: ")
        if answer.lower() == "n":
            print(pgm(answer))
            exit()
        elif answer.lower() == "y":
            break
        else:
            print(pgm(answer))
    except ValueError:
        print("Please enter only letters.")
        exit()

ld()

def signup():
    print("Personal Details: (Sign-In)")

    while True:
        email = input("Provide email address: ")
        match = re.match(r"^[a-zA-Z0-9._%+-]+@(gmail|yahoo|protonmail|outlook|aol|zoho|iCloud|yahoo!|gmx)\.[a-zA-Z]{2,}$", email)

        if match:
            print("Your email is Saved!")
            break

        else:
            print("Access Denied. Please enter another valid email.")

    while True:
        password = input("Enter a strong password (Should be at least 8 characters and numbers): ")
        if len(password) < 8:
            print("Access Denied. Password should be at least 8 characters.")
            continue
        match = re.search(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$', password)

        if match:
            print("Your password is saved!")
            print("Login to Continue")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            f2[email] = hashed_password
            break

        else:
            print("Invalid password. Please enter a valid password.")

def home():
    time.sleep(1)
    print()

    def wlc2():
        for d in "Welcome to Kear's Restaurant Website!\nSharing is Kearing~":
            time.sleep(0.1)
            print(d, end="")
        print()

    wlc2()
    n = datetime.datetime.now()
    time.sleep(1)
    v = ("\nDate and time as of right now:")
    print(v, n)

print()

def dl():
    c = "Launching Application"
    print(c, end="")
    for a in "...":
        time.sleep(0.5)
        print(a, end="")
    print()
dl()

f2 = {}
signup()
home()

def ls():
    loading_window = tk.Tk()

    loading_window.geometry('500x700')

    loading_window.title('Loading')

    loading_label = tk.Label(loading_window, text='Program is Now Loading...', font=('Barlow', 30, 'italic'))
    loading_label.pack(pady=20)

    loading_window.after(3000, loading_window.destroy) # destroy the loading screen after 3 seconds

    loading_window.mainloop()

ls()

w = Tk()
w.title("Kear's Reastaurant")
w.minsize(width=500, height=700)
w.configure(bg="yellow")

def button_clicker():
    breakfast_total = int(breakfast_sb.get()) * 5
    lunch_total = int(lunch_sb.get()) * 15
    dinner_total = int(dinner_sb.get()) * 30
    water_total = int(water_sb.get()) * 3
    juice_total = int(juice_sb.get()) * 1
    coffee_total = int(coffee_sb.get()) * 2

    # =----------List on where you can see on how to pay your order~----------=

    food_list = breakfast_total + lunch_total + dinner_total + water_total + juice_total + coffee_total
    bills_paid = Label(text=f"Your total bill: ₱{food_list}", font=("Barlow", 18 , "Bold"), bg="yellow")
    bills_paid.place(x=150, y=600)

# =----------Application name label----------=

name = Label(text="GREETINGS!\nWELCOME TO\nKEAR'S RESTAURANT", font=("Barlow", 40, "italic"), bg="yellow")
name.grid(column=1, row=0)

# =----------Application name label 2----------=

quote = Label(text="Sharing is Kearing", font=("Barlow", 18, "bold"), bg="yellow")
quote.grid(column=1, row=2)

# =----------Food names----------=

food = Label(text="Choose Your Food", font=("Barlow", 20,"normal"), bg="yellow")

# Breakfast food Image and Its description

breakfast = PhotoImage (file="breakfast.gif")

breakfast_label = Label(image=breakfast, borderwidth=0)

breakfast_label.place(x=50, y=130)

breakfast_information = Label(text="2pcs of Hotdog and Egg W/ Rice\n₱160", font=("Barlow", 15, "normal"), bg="yellow")

breakfast_information.place(x=40, y=230)

breakfast_sb = Spinbox(from_=0, to=10, width=5)

breakfast_sb.place(x=80, y=270)

# =----------Lunch  food Image and Its description----------=

lunch = PhotoImage (file="lunch.gif")

lunch_label = Label(image=lunch, borderwidth=0)

lunch_label.place(x=200, y=130)

lunch_information = Label(text="ALL Food buffet\nUNLIMITED RICE\n₱300", font=("Barlow", 15, "normal"), bg="yellow")

lunch_information.place(x=210, y=230)

lunch_sb = Spinbox(from_=0, to=10, width=5)

lunch_sb.place(x=225, y=270)

# =----------Dinner food Image and Its description----------=

dinner = PhotoImage (file="dinner.gif")

dinner_label = Label(image=dinner, borderwidth=0)

dinner_label.place(x=350, y=130)

dinner_information = Label(text="Unlimited Dinner Family Pan\n₱400", font=("Barlow", 15, "normal"), bg="yellow")

dinner_information.place(x=350, y=130)

dinner_sb = Spinbox(from_=0, to=10, width=5)

dinner_sb.place(x=380, y=270)

# =----------Bevarages names----------=

bevarages = Label(text="Choose Your Drinks", font=("Barlow", 20,"normal"), bg="yellow")
bevarages.place(x=0, y=350)

# =----------Water and Its description----------=

water = PhotoImage (file="water.gif")

water = Label(image=water, borderwidth=0)

water.place(x=50, y=380)

water_information = Label(text="Unlimited Water\n₱10", font=("Barlow", 15, "normal"), bg="yellow")

water_information.place(x=40, y=480)

water_sb = Spinbox(from_=0, to=10, width=5)

water_sb.place(x=80, y=520)

# =----------Juices And Bevarages and Its description----------=

juice = PhotoImage (file="juice.gif")

juice = Label(image=juice, borderwidth=0)

juice.place(x=200, y=380)

juice_information = Label(text="ALL kinds fo juices and Bevarages\n₱80", font=("Barlow", 15, "normal"), bg="yellow")

juice_information.place(x=225, y=480)

juice_sb = Spinbox(from_=0, to=10, width=5)

juice_sb.place(x=230, y=520)

# =----------Coffee and Its description----------=
coffee = PhotoImage (file="coffee.gif")

coffee = Label(image=coffee, borderwidth=0)

coffee.place(x=350, y=380)

coffee_information = Label(text="\n₱70", font=("Barlow", 15, "normal"), bg="yellow")

coffee_information.place(x=360, y=480)

coffee_sb = Spinbox(from_=0, to=10, width=5)

coffee_sb.place(x=375, y=520)

# =----------For the ending button----------=

finish = Button(text="Order", command=button_clicker)

w.mainloop()




