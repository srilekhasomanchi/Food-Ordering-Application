import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from MySql_queries import DataBase
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from common_functions import *
from classes import *
from datetime import datetime

def login_page(parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Login page')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    background_image = ImageTk.PhotoImage(Image.open('Images/login-background.jpeg').resize((window_width+100,window_height),Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    root.resizable(False,False)

    def login_clicked(email, password):
        if db.user_login(email, password):
            login_as_page(email, root, db)

        else:
            showinfo(
                title = 'Error',
                message = 'Email and Password does not match'
            )

    def register_clicked():
        register_page(root, db)

    login_frame = Frame(root, bg="white")
    login_frame.place(x=window_width//15, y=(window_height//4), height = window_height//2, width = 3*window_width//7)

    email_label = Label(login_frame, text="Email", font = ("Goudy old style",17,"bold"),fg="grey",bg="white")
    email_entry = Entry(login_frame,font=("times new roman",15),bg="lightgray")
    email_entry.focus()
    pass_label = Label(login_frame, text="Password", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    pass_entry = Entry(login_frame, font=("times new roman", 15), bg="lightgray",show="*")
    email_label.place(y = 2*window_height//20,x =  window_width//30)
    email_entry.place(y = 2*window_height//20,x = 2.2*window_width//20,width = 2*window_width//5-130)
    pass_label.place(y = 3.5*window_height//20,x =  window_width//30)
    pass_entry.place(y = 3.5*window_height//20,x =  2.2*window_width//20,width = 2*window_width//5-130)

    login_button = Button(login_frame, text="Login", command=lambda:login_clicked(email_entry.get(), pass_entry.get()), font = ("Ariel 15 bold"))
    login_button.place(x = window_width//30,y = 5*window_height//20,height = window_height//15,width = 2*window_width//5-35)

    register_button = Button(login_frame, text="Register", command=register_clicked, font = ("Ariel 15 bold"))
    register_button.place(x = window_width//30,y = 7*window_height//20,height = window_height//15,width = 2*window_width//5-35)

    root.mainloop()

def register_page(parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Register page')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/register-background.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    register_frame = Frame(root, bg="white")
    register_frame.place(x=window_width // 30, y=(window_height // 4), height=3*window_height //5,
                      width=4 * window_width // 9)

    name_label = Label(register_frame, text="Name", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    name_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    name_entry.focus()
    mobile_label = Label(register_frame, text="Mobile No.", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    mobile_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    email_label = Label(register_frame, text="Email", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    email_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    pass_label = Label(register_frame, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    pass_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray", show="*")
    name_label.place(y=2 * window_height // 20, x=window_width // 30)
    name_entry.place(y=2 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    mobile_label.place(y=3.5 * window_height // 20, x=window_width // 30)
    mobile_entry.place(y=3.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    email_label.place(y=5 * window_height // 20, x=window_width // 30)
    email_entry.place(y=5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    pass_label.place(y=6.5 * window_height // 20, x=window_width // 30)
    pass_entry.place(y=6.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)

    def register_clicked():
        name = name_entry.get()
        email = email_entry.get()
        password = pass_entry.get()
        mobile = mobile_entry.get()
        msg = ''
        if not check_length_less_than(name,100):
            msg = 'Name is too long'
        elif not is_numeric(mobile):
            msg = 'Enter a valid mobile number'
        elif len(mobile) != 10:
            msg = 'Enter a valid mobile number'
        if len(msg) != 0:
            showinfo(
                title='Error',
                message=msg
            )
            return
        if not db.insert_user(name_entry.get(), email_entry.get(), pass_entry.get(), mobile_entry.get()):
            showinfo(
                title='Error',
                message='Email or mobile number already exists'
            )
            return
        showinfo(
            title='Success',
            message='Successfully registered'
        )
        login_page(root, db)


    def login_clicked():
        login_page(root, db)

    login_button = Button(register_frame, text="Register", command=register_clicked, font=("Ariel 15 bold"))
    login_button.place(x=window_width // 30, y=8 * window_height // 20, height=window_height // 15,
                       width=2 * window_width // 5 - 35)

    register_button = Button(register_frame, text="Already have an account?", command=login_clicked, font=("Ariel 15 bold"))
    register_button.place(x=window_width // 30, y=9.7 * window_height // 20, height=window_height // 15,
                          width=2 * window_width // 5 - 35)

    root.mainloop()

def login_as_page(email, parent_window = None,db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Login page')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (1*screen_width)//3
    window_height = (1*screen_height)//3

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False,False)

    def login_as_customer_clicked():
        details = db.get_user_details(email)
        customer = User(email, details[0], details[1], details[2])
        customer_home_page(customer, root, db)

    def login_as_manager_clicked():

        details = db.get_user_details(email)
        manager = Manager(email, details[0], details[1], details[2], details[3])
        manager_home_page(manager, root, db)
    def login_as_delivery_person_clicked():
        details = db.get_user_details(email)
        customer = User(email, details[0], details[1], details[2], details[3])
        delivery_person_homepage(customer, root, db)

    login_customer_button = Button(root, text="Login as Customer", command=login_as_customer_clicked, font=("Ariel 15 bold"))
    login_customer_button.place(x=window_width // 8, y=1.5 * window_height // 10, height=window_height // 5,
                       width=3 * window_width // 4 - 10)

    login_manager_button = Button(root, text="Login as Manager", command=login_as_manager_clicked, font=("Ariel 15 bold"))
    login_manager_button.place(x=window_width // 8, y=4 * window_height // 10, height=window_height // 5,
                          width=3 * window_width // 4 - 10)

    login_delivery_person_button = Button(root, text="Login as Delivery Person", command=login_as_delivery_person_clicked, font=("Ariel 15 bold"))
    login_delivery_person_button.place(x=window_width // 8, y=6.5 * window_height // 10, height=window_height // 5,

                       width=3 * window_width // 4 - 10)
    root.mainloop()

def add_restaurant_page(manager, parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Register restaurant')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/manager_home_page_background.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    cities = db.get_all_cities()

    frame = Frame(root, bg="white")

    city_clicked = StringVar()
    area_clicked = StringVar()

    city_clicked.set(cities[0])
    areas = db.get_areas_in_city(cities[0])
    area_clicked.set(areas[0])

    frame.place(x=window_width//15, y=(window_height//6), height = 540, width = 4*window_width//7)


    name_label = Label(frame, text="Restaurant name", font = ("Goudy old style",17,"bold"),fg="grey",bg="white")
    name_entry = Entry(frame,font=("times new roman",15),bg="lightgray")
    name_entry.focus()
    opening_label = Label(frame, text="Opening time", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    opening_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable = StringVar(root,"09:00"))
    closing_label = Label(frame, text="Closing time", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    closing_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable = StringVar(root,"22:30"))
    city_label = Label(frame, text="City", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    city_entry = OptionMenu(frame, city_clicked, *cities)
    area_label = Label(frame, text="Area", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    area_entry = OptionMenu(frame, area_clicked, *areas)
    address_label = Label(frame, text="Address", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    address_entry = Entry(frame, font=("times new roman", 15), bg="lightgray")
    phone_label = Label(frame, text="Phone", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    phone_entry = Entry(frame, font=("times new roman", 15), bg="lightgray")
    note_msg = "Note: Enter the time in HH:MM format. For example, 4 hours 20 minutes can be entered as 04:20."
    note_label = Label(frame, text = note_msg, font = ("Goudy old style", 12), fg = "grey", bg = "white")

    def check(event):
        nonlocal areas
        nonlocal area_entry
        nonlocal area_clicked
        areas = db.get_areas_in_city(city_clicked.get())
        if area_clicked.get() not in areas:
            area_clicked.set(areas[0])
        area_entry = OptionMenu(frame, area_clicked, *areas)
        area_entry.place(y=240, x=240, width=350, height=30)
        area_entry.bind('<Enter>', check)

    area_entry.bind('<Enter>', check)

    name_label.place(y = 60,x =  40)
    name_entry.place(y = 60,x = 240,width = 350, height = 30)
    opening_label.place(y = 120,x = 40)
    opening_entry.place(y = 120,x =  190,width = 150,height = 30)
    closing_label.place(y = 120,x =  360)
    closing_entry.place(y=120, x=510, width=150,height = 30)
    city_label.place(y=180, x=40)
    city_entry.place(y=180, x=240, width=350, height=30)
    area_label.place(y=240,x=40)
    area_entry.place(y=240,x=240,width=350,height=30)
    address_label.place(y=300, x=40)
    address_entry.place(y=300, x=240, width=350, height=30)
    phone_label.place(y=360, x=40)
    phone_entry.place(y=360, x=240, width=350, height=30)
    note_label.place(y = 480,x = 40)

    def register_clicked():
        open = opening_entry.get()
        close = closing_entry.get()
        phone = phone_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        msg = ""
        if(len(open)!=5 or len(close)!=5 or open[2] != ':' or close[2] != ':'):
            msg = "Please enter a valid time"
        (open_hours,open_minutes,close_hours,close_minutes) = (None,None,None,None)
        if msg == "" and ((not is_numeric(open[0:2]) )or (not is_numeric(close[0:2])) or (not is_numeric(open[3:5])) or (not is_numeric(close[3:5]))):
            msg = "Please enter a valid time"
        if len(msg) == 0:
            (open_hours,open_minutes) = get_hours_minutes_from_time(open)
            (close_hours,close_minutes) = get_hours_minutes_from_time(close)
        if msg == "" and max(open_hours,close_hours) > 23:
            msg = "Please enter a valid time"
        if msg == "" and max(open_minutes, close_minutes) > 59:
            msg = "Please enter a valid time"
        if msg == "" and ((not is_numeric(phone)) or len(phone) != 10):
            msg = "Please enter a valid phone number"
        if msg == "" and len(name) < 4:
            msg = "Restaurant name must contain at least 4 characters"
        if msg == "" and len(address) < 10:
            msg = "Address field must contain at least 10 characters"

        if len(msg) != 0:
            showinfo(
                title = "Error",
                message = msg
            )
            return

        result = db.insert_restaurant(manager.email,name,open,close,address,area_clicked.get(),city_clicked.get(),phone)

        if result == 1:
            msg = "There exists a restaurant with the same name and in the same area."
        elif result == 2:
            msg = "The given phone number already exists."

        if len(msg) != 0:
            showinfo(
                title = "Error",
                message = msg
            )
            return

        msg = "Restaurant successfully added."
        showinfo(
            title = "Success",
            message = msg
        )
        manager_home_page(manager,root,db)

    def cancel_clicked():
        manager_home_page(manager, root, db)

    register_button = Button(frame, text="Register", command=register_clicked, font = ("Ariel 15 bold"))
    register_button.place(x = 40,y = 420,height = 40,width = 250)

    cancel_button = Button(frame, text="Cancel", command=cancel_clicked, font = ("Ariel 15 bold"))
    cancel_button.place(x = 340,y = 420,height = 40,width = 250)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root,db), font=("Ariel 15 bold"))
    logout_button.place(x=24*window_width // 30, y=window_height // 20, height=window_height // 15,
                          width=1 * window_width // 5 - 35)

    root.mainloop()

def manager_home_page(manager, parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Manage restaurant')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/manager_home_page_background.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)



    details = db.get_restaurant_details_managed_by(manager.email)
    frame = Frame(root, bg="white")
    frame.place(x=window_width // 15, y=(window_height // 4), height=window_height // 3,
                      width=4 * window_width // 9)

    def add_restaurant_clicked():
        add_restaurant_page(manager,root,db)


    if details == None:
        label = Label(frame, text="You are not a manager of any restaurant", font=("Goudy old style", 20, "bold"), fg="grey", bg="white")
        label.place(y=2 * window_height // 20, x=window_width // 30)
        add_restaurant_button = Button(frame, text="Add a restaurant", command=add_restaurant_clicked, font = ("Ariel 15 bold"))
        add_restaurant_button.place(x = window_width//30,y = 3.5*window_height//20,height = window_height//15,width = 2*window_width//5-35)
    else:

        restaurant = Restaurant(details[0],details[1],details[2],details[3],details[4],details[5],details[6],details[7],convert_string_to_bool(details[8]))
        email_label = Label(frame, text="Restaurant name: {0}".format(details[2]), font=("Goudy old style", 20, "bold"),
                            fg="grey", bg="white")
        email_label.place(y=2 * window_height // 20, x=window_width // 30)
        manage_restaurant_button = Button(frame, text="Manage", command=lambda: manage_restaurant_page(restaurant,root,db),
                                       font=("Ariel 15 bold"))
        manage_restaurant_button.place(x=window_width // 30, y=3.5 * window_height // 20, height=window_height // 15,
                                    width=2 * window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    root.mainloop()

def manage_restaurant_page(restaurant,parent_window = None,db = None, page_number = 0):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Manage restaurant')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)

    data = db.get_food_items(restaurant.id)
    restaurant.foodItems = []

    for x in data:
        new_food_item = FoodItem(x[0], x[1], x[2], x[3], x[5], convert_string_to_bool(x[4]))
        restaurant.addFoodItem(new_food_item)

    background_image = ImageTk.PhotoImage(
        Image.open('Images/manager_home_page_background.jpg').resize((window_width + 100, window_height),
                                                                     Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    frames = []

    num_pages = (len(restaurant.foodItems)+5)//6

    if len(restaurant.foodItems) == 0:
        no_label = Label(root, text="Currently no food items to display", font=("Goudy old style", 18, "bold"), fg="grey", bg="white")
        no_label.place(x = window_width//2-200,y = 50)

    for j in range(6*page_number, min(6*page_number+6, len(restaurant.foodItems))):
        i = j-(6*page_number)
        xval = 30 + (i % 3)*350
        yval = 50 + (i // 3)*320
        new_frame = Frame(root, bg="white")
        new_frame.place(x=xval, y=yval, height=270, width=300)

        entry_frame = Frame(new_frame, bg="white")
        entry_frame.place(x=0, y=0, height=150, width=300)

        name_label = Label(entry_frame, text="Name: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value.insert('1.0',restaurant.foodItems[j].name)
        name_value['state'] = 'disabled'
        availability_label = Label(entry_frame, text="Availability: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        availability_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        availability_value.insert('1.0', convert_availability_to_string(restaurant.foodItems[j].availability))
        availability_value['state'] = 'disabled'
        price_label = Label(entry_frame, text="Price: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        price_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        price_value.insert('1.0', str(restaurant.foodItems[j].price))
        price_value['state'] = 'disabled'
        name_label.place(x=10, y=30)
        name_value.place(x=110, y=30, width=180)
        availability_label.place(x=10, y=70)
        availability_value.place(x=110, y=70, width=180)
        price_label.place(x=10, y=110)
        price_value.place(x=110, y=110, width=180)

        def info_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6*page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            showinfo(
                title='Information',
                message=restaurant.foodItems[ind].description
            )

        def edit_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6*page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            manage_food_item(restaurant, restaurant.foodItems[ind], root, db)

        edit_button = Button(new_frame, text="Edit", command=edit_clicked, font=("Ariel 15 bold"))
        edit_button.place(x=20, y=210, height=40, width=170)

        info_button = Button(new_frame, text="More info", command=info_clicked, font=("Ariel 15 bold"))
        info_button.place(x=20, y=160, height=40, width=170)

        frames.append(new_frame)

    def page_clicked():
        x = root.winfo_pointerx()
        ind = ((x-window_width//2+100)+70)//60
        ind -= 3
        manage_restaurant_page(restaurant, root, db, ind)

    if num_pages > 1:
        for i in range(num_pages):
            color = "white"
            if i == page_number:
                color = "grey"
            button = Button(root, text=str(i+1), command=page_clicked, font=("Ariel 15 bold"), bg = color)
            button.place(x=window_width//2+i*60-100, y=window_height-70, height=30, width=50)

    add_food_item_button = Button(root, text="Add Food Item", command=lambda: add_food_item_page(restaurant,root, db), font=("Ariel 15 bold"))
    add_food_item_button.place(x=24 * window_width // 30, y=3*window_height // 20, height=window_height // 15,
                        width=1*window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1*window_width // 5 - 35)

    root.mainloop()

def manage_food_item(restaurant, fooditem, parent_window, db):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Manage food item')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/manager_home_page_background.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    frame = Frame(root, bg="white")

    frame.place(x=window_width//15, y=(window_height//6), height=540, width=4*window_width//7)

    availability_clicked = StringVar()
    availability_clicked.set(convert_availability_to_string(fooditem.availability))

    options = ['Available', 'Not available']

    name_label = Label(frame, text="Name", font=("Goudy old style",17,"bold"),fg="grey",bg="white")
    name_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable = StringVar(root,fooditem.name))
    name_entry.focus()
    description_label = Label(frame, text="Description", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    description_entry = Text(frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
    description_entry.insert('1.0', fooditem.description)
    price_label = Label(frame, text="Price", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    price_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable = StringVar(root,str(fooditem.price)))
    availability_label = Label(frame, text="Availability", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    availability_entry = OptionMenu(frame, availability_clicked, *options)

    def ok_clicked():
        name = name_entry.get()
        price = price_entry.get()
        msg = ""
        if len(name) < 4:
            msg = "Food item name should contain at least 4 characters"
        if msg == "" and (not is_double(price)):
            msg = "Enter a valid price"

        if msg != "":
            showinfo(
                title='Error',
                message=msg
            )
            return
        availability = ""
        if availability_clicked.get() == "Available":
            availability = 'True'
        else:
            availability = 'False'
        db.edit_food_item(fooditem.food_id, name, description_entry.get('1.0', 'end'), price, availability)
        showinfo(
            title='Success',
            message='Food item got successfully updated'
        )
        manage_restaurant_page(restaurant, root, db)

    ok_button = Button(frame, text="OK", command=ok_clicked, font=("Ariel 15 bold"))
    ok_button.place(x=40, y=380, height=40, width=250)

    def cancel_clicked():
        manage_restaurant_page(restaurant, root, db)

    def delete_clicked():
        answer = askyesno(title='confirmation',
                          message='Are you sure that you want to delete this item?')
        if answer:
            db.delete_food_item(fooditem.food_id)
            manage_restaurant_page(restaurant, root, db)

    name_label.place(y=60, x=40)
    name_entry.place(y=60, x=240, width=350, height=30)
    description_label.place(y=120, x=40)
    description_entry.place(y=120, x=240, width=450, height=90)
    price_label.place(y=240, x=40)
    price_entry.place(y=240, x=240, width=350, height=30)
    availability_label.place(y=300, x=40)
    availability_entry.place(y=300, x=240, width = 350, height = 30)

    cancel_button = Button(frame, text="Cancel", command=cancel_clicked, font = ("Ariel 15 bold"))
    cancel_button.place(x=340, y=380, height=40, width=250)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24*window_width // 30, y=window_height // 20, height=window_height // 15, width=1 * window_width // 5 - 35)

    delete_button = Button(frame, text="Delete this item", command=delete_clicked, font=("Ariel 15 bold"))
    delete_button.place(x=120, y=450, height=40, width=350)

    root.mainloop()

def add_food_item_page(restaurant, parent_window = None, db = None):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Add Food Item')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/manager_home_page_background.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    frame = Frame(root, bg="white")

    frame.place(x=window_width // 15, y=(window_height // 6), height=360, width=4 * window_width // 7)

    name_label = Label(frame, text="Food name", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    name_entry = Entry(frame, font=("times new roman", 15), bg="lightgray")
    name_entry.focus()
    description_label = Label(frame, text="Description", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    description_entry = Text(frame, font=("times new roman", 14), bg="lightgray")
    price_label = Label(frame, text="Price", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    price_entry = Entry(frame, font=("times new roman", 15), bg="lightgray")

    def add_clicked():
        name = name_entry.get()
        price = price_entry.get()
        msg = ""
        if len(name) < 4:
            msg = "Food item name should contain at least 4 characters"
        if msg == "" and (not is_double(price)):
            msg = "Enter a valid price"

        if msg != "":
            showinfo(
                title='Error',
                message=msg
            )
            return
        db.insert_food_item(restaurant.id, name, description_entry.get('1.0', 'end'), price)
        showinfo(
            title='Success',
            message='Food item successfully added to the restaurant menu'
        )
        manage_restaurant_page(restaurant, root, db)

    add_button = Button(frame, text="Add Food Item", command=add_clicked, font=("Ariel 15 bold"))
    add_button.place(x=40, y=280, height=40, width=250)

    cancel_button = Button(frame, text="Cancel", command=lambda: manage_restaurant_page(restaurant,root,db), font=("Ariel 15 bold"))
    cancel_button.place(x=340, y=280, height=40, width=250)

    name_label.place(y=60, x=40)
    name_entry.place(y=60, x=240, width=350, height=30)
    description_label.place(y=120, x=40)
    description_entry.place(y=120, x=240, width=450, height=70)
    price_label.place(y=220, x=40)
    price_entry.place(y=220, x=240, width=350, height=30)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    root.mainloop()

def add_address(user, parent_window=None, db=None):
    if db == None:
        db = DataBase()
    if (parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Add your address')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (2 * screen_width) // 3
    window_height = (2 * screen_height) // 3

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/address.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    cities = db.get_all_cities()

    frame = Frame(root, bg="white")

    city_clicked = StringVar()
    area_clicked = StringVar()

    city_clicked.set(cities[0])
    areas = db.get_areas_in_city(cities[0])
    area_clicked.set(areas[0])

    frame.place(x=window_width // 15, y=(window_height // 6), height=350, width=4 * window_width // 7)

    city_label = Label(frame, text="City", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    city_entry = OptionMenu(frame, city_clicked, *cities)
    area_label = Label(frame, text="Area", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    area_entry = OptionMenu(frame, area_clicked, *areas)
    address_label = Label(frame, text="Address", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    address_entry = Text(frame, font=("times new roman", 15), bg="lightgray")

    def check(event):
        nonlocal areas
        nonlocal area_entry
        nonlocal area_clicked
        areas = db.get_areas_in_city(city_clicked.get())
        if area_clicked.get() not in areas:
            area_clicked.set(areas[0])
        area_entry = OptionMenu(frame, area_clicked, *areas)
        area_entry.place(y=120, x=140, width=250, height=30)
        area_entry.bind('<Enter>', check)

    area_entry.bind('<Enter>', check)

    city_label.place(y=50, x=40)
    city_entry.place(y=50, x=140, width=250, height=30)
    area_label.place(y=120, x=40)
    area_entry.place(y=120, x=140, width=250, height=30)
    address_label.place(y=190, x=40)
    address_entry.place(y=190, x=140, width=250, height=50)

    def register_clicked():
        address = address_entry.get('1.0', 'end')
        msg = ""
        if msg == "" and len(address) < 10:
            msg = "Address field must contain at least 10 characters"

        if len(msg) != 0:
            showinfo(
                title="Error",
                message=msg
            )
            return

        result = db.update_user_area(user.email, address, area_clicked.get(), city_clicked.get())

        if result == 1:
            msg = "Profile updated succesfully"

        if len(msg) != 0:
            showinfo(
                title="Success",
                message=msg
            )
            customer_home_page(user, root, db)
            return

        msg = "There is some error while updating address."
        showinfo(
            title="Error",
            message=msg
        )

    register_button = Button(frame, text="Update address", command=register_clicked, font=("Ariel 12 bold"))
    register_button.place(x=150, y=260, height=40, width=150)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=700, y=20)

    root.mainloop()

def edit_profile(user, parent_window=None, db=None):
    if db == None:
        db = DataBase()
    if (parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Your profile')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (2 * screen_width) // 3
    window_height = (3 * screen_height) // 4

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/profile.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    cities = db.get_all_cities()

    frame = Frame(root, bg="white")

    city_clicked = StringVar()
    area_clicked = StringVar()

    city_clicked.set(cities[0])
    areas = db.get_areas_in_city(cities[0])
    area_clicked.set(areas[0])

    frame.place(x=window_width // 12, y=(window_height // 15), height=450, width=4 * window_width // 7)

    name_label = Label(frame, text="Name", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    name = StringVar(root, value=user.name)
    name_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=name)
    mobile_label = Label(frame, text="Mobile No", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    mobile = StringVar(root, value=user.contact)
    mobile_entry = Entry(frame, font=("times new roman", 15), bg="lightgray", textvariable=mobile)
    city_label = Label(frame, text="City", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    city_entry = OptionMenu(frame, city_clicked, *cities)
    area_label = Label(frame, text="Area", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    area_entry = OptionMenu(frame, area_clicked, *areas)
    address_label = Label(frame, text="Address", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    address_entry = Text(frame, font=("times new roman", 15), bg="lightgray")
    address_entry.insert(END, user.address)

    def check(event):
        nonlocal areas
        nonlocal area_entry
        nonlocal area_clicked
        areas = db.get_areas_in_city(city_clicked.get())
        if area_clicked.get() not in areas:
            area_clicked.set(areas[0])
        area_entry = OptionMenu(frame, area_clicked, *areas)
        area_entry.place(y=260, x=150, width=250, height=30)
        area_entry.bind('<Enter>', check)

    area_entry.bind('<Enter>', check)

    name_label.place(y=50, x=40)
    name_entry.place(y=50, x=150, width=250, height=30)
    mobile_label.place(y=120, x=40)
    mobile_entry.place(y=120, x=150, width=250, height=30)
    city_label.place(y=190, x=40)
    city_entry.place(y=190, x=150, width=250, height=30)
    area_label.place(y=260, x=40)
    area_entry.place(y=260, x=150, width=250, height=30)
    address_label.place(y=330, x=40)
    address_entry.place(y=330, x=150, width=250, height=50)

    def update_clicked():
        address = address_entry.get('1.0', 'end')
        name = name_entry.get()
        mobile = mobile_entry.get()
        msg = ''
        if msg == "" and len(address) < 10:
            msg = "Address field must contain at least 10 characters"
        if not check_length_less_than(name, 100):
            msg = 'Name is too long'
        elif not is_numeric(mobile):
            msg = 'Enter a valid mobile number'
        elif len(mobile) != 10:
            msg = 'Enter a valid mobile number'
        elif mobile != user.contact and db.is_mobile_number_exists(mobile):
            msg = 'Mobile number already exists'
        if len(msg) != 0:
            showinfo(
                title="Error",
                message=msg
            )
            return

        result = db.update_user_profile(user.email, name_entry.get(), mobile_entry.get(), address, area_clicked.get(),
                                        city_clicked.get())

        if result == 1:
            msg = "Area updated succesfully"

        if len(msg) != 0:
            showinfo(
                title="Success",
                message=msg
            )
            customer_home_page(user, root, db)
            return

        msg = "There is some error while updating address."
        showinfo(
            title="Error",
            message=msg
        )

    register_button = Button(frame, text="Update profile", command=update_clicked, font=("Ariel 12 bold"))
    register_button.place(x=150, y=400, height=40, width=150)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=700, y=20)

    logout_button = Button(root, text="Cancel", command=lambda: customer_home_page(user, root, db), font=("Ariel 15 bold"))
    logout_button.place(x=700, y=70)

    root.mainloop()

def customer_home_page(user, parent_window=None, db=None, page_number = 0):
    if db == None:
        db = DataBase()

    details = db.get_user_details(user.email)
    user = User(user.email, details[0], details[1], details[2], details[3])
    areaid = user.area_id
    if (parent_window != None):
        parent_window.destroy()
    root = tk.Tk()

    if (areaid == None):
        add_address(user, root, db)

    root.title("Order your food")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6 * screen_width) // 7
    window_height = (6 * screen_height) // 7

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/cus.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    avbl_restaurants = db.restaurants_by_city(areaid)
    restaurants = []
    for x in avbl_restaurants:
        restaurants.append(Restaurant(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7],convert_string_to_bool(x[8])))


    for i in range(len(restaurants)):
        s = restaurants[i].open_time
        restaurants[i].open_time = mytime(int(s[0:2]), int(s[3:5]))
        s = restaurants[i].close_time
        restaurants[i].close_time = mytime(int(s[0:2]), int(s[3:5]))

    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cur_time = mytime(int(current_time[0:2]),int(current_time[3:5]))

    status = []

    for x in restaurants:
        if are_times_consequent(x.open_time,cur_time,x.close_time):
            status.append(1)
        else:
            status.append(0)

    for i in range(len(restaurants)):
        if restaurants[i].flag:
            status[i] ^= 1

    open_restaurants = []
    closed_restaurants = []

    for i in range(len(restaurants)):
        if status[i]:
            open_restaurants.append(restaurants[i])
        else:
            closed_restaurants.append(restaurants[i])

    restaurants = []
    status = []
    for x in open_restaurants:
        restaurants.append(x)
        status.append(True)
    for x in closed_restaurants:
        restaurants.append(x)
        status.append(False)

    num_pages = (len(restaurants) + 5) // 6

    for j in range(6 * page_number, min(6 * page_number + 6, len(restaurants))):
        i = j - (6 * page_number)
        xval = 30 + (i % 3) * 350
        yval = 50 + (i // 3) * 320
        new_frame = Frame(root, bg="white")
        new_frame.place(x=xval, y=yval, height=270, width=300)

        entry_frame = Frame(new_frame, bg="white")
        entry_frame.place(x=0, y=0, height=110, width=300)

        name_label = Label(entry_frame, text="Name: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value.insert('1.0', restaurants[j].name)
        name_value['state'] = 'disabled'
        timings_label = Label(entry_frame, text="Timings: ", font=("Goudy old style", 12, "bold"), fg="grey",
                                   bg="white")
        timings_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        timings_value.insert('1.0', str(restaurants[j].open_time.hours) + ':' + str(restaurants[j].open_time.minutes) + " - " + str(restaurants[j].close_time.hours) + ':' + str(restaurants[j].close_time.minutes))
        timings_value['state'] = 'disabled'
        val = "Currently closed"
        color = "#FFB3B3"
        if status[j]:
            val = "Open"
            color = "#CCFFCC"
        status_label = Label(new_frame, text=val, font=("Goudy old style", 15, "bold"), fg="grey", bg=color)
        name_label.place(x=10, y=30)
        name_value.place(x=110, y=30, width=180)
        timings_label.place(x=10, y=70)
        timings_value.place(x=110, y=70, width=180)
        status_label.place(x=70, y=120, width = 150)

        def info_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            msg = ""
            msg += "Area: " + db.get_area_by_areaid(restaurants[ind].area_id)
            msg += '\n'
            msg += "Address : " + restaurants[ind].address
            msg += '\n'
            msg += "Phone : " + restaurants[ind].phone
            showinfo(
                title='Information',
                message=msg
            )

        def view_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            view_restaurant_page(user, restaurants[ind],root,db,0)

        view_button = Button(new_frame, text="View", command=view_clicked, font=("Ariel 15 bold"))
        if status[j]:
            view_button.place(x=20, y=210, height=40, width=170)

        info_button = Button(new_frame, text="More info", command=info_clicked, font=("Ariel 15 bold"))
        info_button.place(x=20, y=160, height=40, width=170)

    def page_clicked():
        x = root.winfo_pointerx()
        ind = ((x - window_width // 2 + 100) + 70) // 60
        ind -= 3
        customer_home_page(user, root, db, ind)

    if num_pages > 1:
        for i in range(num_pages):
            color = "white"
            if i == page_number:
                color = "grey"
            button = Button(root, text=str(i + 1), command=page_clicked, font=("Ariel 15 bold"), bg=color)
            button.place(x=window_width // 2 + i * 60 - 100, y=window_height - 70, height=30, width=50)


    profile_button = Button(root, text="Edit profile", command=lambda: edit_profile(user, root, db),
                            font=("Ariel 15 bold"))
    profile_button.place(x=24* window_width // 30, y=3*window_height // 20, height=window_height // 15,
                         width=1 * window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    my_orders_button = Button(root, text="My orders", command=lambda: my_orders_customer(user, root, db), font=("Ariel 15 bold"))
    my_orders_button.place(x=24 * window_width // 30, y=7*window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    def cart_clicked():
        cart_page(user, root, db, 0)

    go_to_cart_button = Button(root, text="Display cart", command = cart_clicked, font=("Ariel 15 bold"))
    go_to_cart_button.place(x=24 * window_width // 30, y=5*window_height // 20, height=window_height // 15,
    width = 1 * window_width // 5 - 35)

    root.mainloop()

def view_restaurant_page(user, restaurant, parent_window = None, db = None, page_number = 0):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Select food items')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)

    data = db.get_food_items(restaurant.id)
    restaurant.foodItems = []

    for x in data:
        new_food_item = FoodItem(x[0], x[1], x[2], x[3], x[5], convert_string_to_bool(x[4]))
        restaurant.addFoodItem(new_food_item)

    background_image = ImageTk.PhotoImage(
        Image.open('Images/cus.jpg').resize((window_width + 100, window_height),
                                                                     Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    frames = []

    if len(restaurant.foodItems) == 0:
        no_label = Label(root, text="Currently no food items to display", font=("Goudy old style", 18, "bold"), fg="grey", bg="white")
        no_label.place(x = window_width//2-200,y = 50)

    num_pages = (len(restaurant.foodItems)+5)//6

    def cart_clicked():
        cart_page(user, root, db, 0)

    def info_clicked():
        x = root.winfo_pointerx()
        y = root.winfo_pointery()
        ind = 6 * page_number
        if y > 500:
            ind += 3
        if x > 730:
            ind += 2
        elif x > 380:
            ind += 1
        showinfo(
            title='Information',
            message=restaurant.foodItems[ind].description
        )

    def add_to_cart_clicked():
        x = root.winfo_pointerx()
        y = root.winfo_pointery()
        ind = 6 * page_number
        if y > 500:
            ind += 3
        if x > 730:
            ind += 2
        elif x > 380:
            ind += 1
        db.add_to_cart(user.email, restaurant.foodItems[ind].food_id)
        showinfo(
            title='Success',
            message='Item successfully added to the cart'
        )

    for j in range(6*page_number, min(6*page_number+6, len(restaurant.foodItems))):
        i = j-(6*page_number)
        xval = 30 + (i % 3)*350
        yval = 50 + (i // 3)*320
        new_frame = Frame(root, bg="white")
        new_frame.place(x=xval, y=yval, height=270, width=300)

        entry_frame = Frame(new_frame, bg="white")
        entry_frame.place(x=0, y=0, height=110, width=300)

        name_label = Label(entry_frame, text="Name: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value.insert('1.0',restaurant.foodItems[j].name)
        name_value['state'] = 'disabled'
        availability_label = Label(entry_frame, text="Availability: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        availability_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        availability_value.insert('1.0', convert_availability_to_string(restaurant.foodItems[j].availability))
        availability_value['state'] = 'disabled'
        price_label = Label(entry_frame, text="Price: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        price_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        price_value.insert('1.0', str(restaurant.foodItems[j].price))
        price_value['state'] = 'disabled'
        name_label.place(x=10, y=30)
        name_value.place(x=110, y=30, width=180)
        price_label.place(x=10, y=70)
        price_value.place(x=110, y=70, width=180)

        val = "Currently unaivalable"
        color = "#FFB3B3"
        if restaurant.foodItems[j].availability:
            val = "Available"
            color = "#CCFFCC"
        status_label = Label(new_frame, text=val, font=("Goudy old style", 15, "bold"), fg="grey", bg=color)
        status_label.place(x=55, y=120, width = 200)

        add_to_cart_button = Button(new_frame, text="Add to cart", command=add_to_cart_clicked, font=("Ariel 15 bold"))
        if val == "Available":
            add_to_cart_button.place(x=20, y=210, height=40, width=170)

        info_button = Button(new_frame, text="More info", command=info_clicked, font=("Ariel 15 bold"))
        info_button.place(x=20, y=160, height=40, width=170)

        frames.append(new_frame)

    go_to_cart_button = Button(root, text="Display cart", command=cart_clicked, font=("Ariel 15 bold"))
    go_to_cart_button.place(x=24 * window_width // 30, y=5 * window_height // 20, height=window_height // 15,
                            width=1 * window_width // 5 - 35)
    def page_clicked():
        x = root.winfo_pointerx()
        ind = ((x-window_width//2+100)+70)//60
        ind -= 3
        view_restaurant_page(user, restaurant, root, db, ind)

    if num_pages > 1:
        for i in range(num_pages):
            color = "white"
            if i == page_number:
                color = "grey"
            button = Button(root, text=str(i+1), command=page_clicked, font=("Ariel 15 bold"), bg = color)
            button.place(x=window_width//2+i*60-100, y=window_height-70, height=30, width=50)

    go_back_button = Button(root, text="Go back", command=lambda: customer_home_page(user,root,db), font=("Ariel 15 bold"))
    go_back_button.place(x=24 * window_width // 30, y=3*window_height // 20, height=window_height // 15,
                        width=1*window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1*window_width // 5 - 35)

    root.mainloop()

def cart_page(user, parent_window = None, db = None, page_number = 0):
    if db == None:
        db = DataBase()
    if(parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Checkout')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6*screen_width)//7
    window_height = (6*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)

    data = db.get_user_cart_items(user.email)

    cart_items = []
    food_items = []

    restaurants = []

    total_price = 0

    for x in data:
        cart_items.append(cart_item(x[0], x[1], x[2]))
        y = db.get_food_item_by_id(x[1])
        food_items.append(FoodItem(y[0], y[1], y[2], y[3], y[5], convert_string_to_bool(y[4])))
        total_price += food_items[-1].price
        if y[1] in restaurants:
            continue
        restaurants.append(y[1])

    background_image = ImageTk.PhotoImage(
        Image.open('Images/cus.jpg').resize((window_width + 100, window_height),
                                                                     Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    frames = []

    if len(food_items) == 0:
        no_label = Label(root, text="Currently no items in the cart to display", font=("Goudy old style", 18, "bold"), fg="grey", bg="white")
        no_label.place(x = window_width//2-200,y = 50)

    num_pages = (len(food_items)+5)//6

    for j in range(6*page_number, min(6*page_number+6, len(food_items))):
        i = j-(6*page_number)
        xval = 30 + (i % 3)*350
        yval = 50 + (i // 3)*320
        new_frame = Frame(root, bg="white")
        new_frame.place(x=xval, y=yval, height=270, width=300)

        entry_frame = Frame(new_frame, bg="white")
        entry_frame.place(x=0, y=0, height=150, width=300)

        name_label = Label(entry_frame, text="Name: ", font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value = Text(entry_frame, font=("Goudy old style", 12, "bold"), fg="grey", bg="white")
        name_value.insert('1.0', food_items[j].name)
        name_value['state'] = 'disabled'
        price_label = Label(entry_frame, text="Price: ", font=("Goudy old style", 16, "bold"), fg="grey", bg="white")
        price_value = Text(entry_frame, font=("Goudy old style", 16, "bold"), fg="grey", bg="white")
        price_value.insert('1.0', str(food_items[j].price))
        price_value['state'] = 'disabled'
        name_label.place(x=10, y=30)
        name_value.place(x=110, y=30, width=180)
        price_label.place(x=10, y=90)
        price_value.place(x=110, y=90, width=180)

        def remove_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            answer = askyesno(
                title='Confirmation',
                message='Are you sure that you want to remove this item from the cart?'
            )
            if answer:
                db.remove_item_from_cart(cart_items[ind].item_id)
                showinfo(
                    title='Success',
                    message='Item successfully removed from the cart.'
                )
                new_page_number = page_number
                if j>0 and 6*page_number == j:
                    new_page_number -= 1
                cart_page(user, root, db, new_page_number)

        remove_button = Button(new_frame, text="Remove", command=remove_clicked, font=("Ariel 15 bold"))
        remove_button.place(x=55, y=190, height=50,
                                width=200)

        frames.append(new_frame)

    def place_clicked():
        if len(restaurants) > 1:
            showinfo(
                title='Error',
                message='Selected food items must be from the same restaurant'
            )
            return
        if len(food_items) != 0:
            food_ids = []
            areaid = db.get_areaid_by_restaurant_id(food_items[0].restaurant_id)
            city = db.city_by_areaid(areaid)
            for x in food_items:
                food_ids.append(x.food_id)
            db.insert_order(user.email, convert_food_ids_to_string(food_ids),city)
            db.remove_from_cart(user.email)
            showinfo(
                title='Success',
                message='Order successfully placed'
            )
            cart_page(user, root, db)

    def page_clicked():
        x = root.winfo_pointerx()
        ind = ((x-window_width//2+100)+70)//60
        ind -= 3
        cart_page(user, root, db, ind)

    if num_pages > 1:
        for i in range(num_pages):
            color = "white"
            if i == page_number:
                color = "grey"
            button = Button(root, text=str(i+1), command=page_clicked, font=("Ariel 15 bold"), bg = color)
            button.place(x=window_width//2+i*60-100, y=window_height-70, height=30, width=50)

    total_price_label = Label(root, text="Total Price: " + str(total_price), font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    total_price_label.place(x=24 * window_width // 30, y=17 * window_height // 20, height=window_height // 15,
           width=1 * window_width // 5 - 35)

    go_back_button = Button(root, text="Go back", command=lambda: customer_home_page(user,root,db), font=("Ariel 15 bold"))
    go_back_button.place(x=24 * window_width // 30, y=3*window_height // 20, height=window_height // 15,
                        width=1*window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1*window_width // 5 - 35)

    place_order_button = Button(root, text="Place order", command=place_clicked, font=("Ariel 15 bold"))
    place_order_button.place(x=24 * window_width // 30, y=5*window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    root.mainloop()

def add_city(user, parent_window=None, db=None):
    if db == None:
        db = DataBase()
    if (parent_window != None):
        parent_window.destroy()
    root = tk.Tk()
    root.title('Select your city')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (2 * screen_width) // 3
    window_height = (2 * screen_height) // 3

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/address.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    cities = db.get_all_cities()

    frame = Frame(root, bg="white")

    city_clicked = StringVar()
    area_clicked = StringVar()

    city_clicked.set(cities[0])
    areas = db.get_areas_in_city(cities[0])
    area_clicked.set(areas[0])

    frame.place(x=window_width // 15, y=(window_height // 6), height=250, width=4 * window_width // 7)

    city_label = Label(frame, text="City", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    city_entry = OptionMenu(frame, city_clicked, *cities)
    area_label = Label(frame, text="Area", font=("Goudy old style", 17, "bold"), fg="grey", bg="white")
    area_entry = OptionMenu(frame, area_clicked, *areas)

    def check(event):
        nonlocal areas
        nonlocal area_entry
        nonlocal area_clicked
        areas = db.get_areas_in_city(city_clicked.get())
        if area_clicked.get() not in areas:
            area_clicked.set(areas[0])
        area_entry = OptionMenu(frame, area_clicked, *areas)
        area_entry.place(y=120, x=140, width=250, height=30)
        area_entry.bind('<Enter>', check)

    area_entry.bind('<Enter>', check)

    city_label.place(y=50, x=40)
    city_entry.place(y=50, x=140, width=250, height=30)
    area_label.place(y=120, x=40)
    area_entry.place(y=120, x=140, width=250, height=30)

    def register_clicked():
        msg = ""

        if city_clicked.get() == "Select your city":
            msg = "Pls select your city and area"

        if len(msg) != 0:
            showinfo(
                title="Error",
                message=msg
            )
            return

        result = db.update_user_city(user.email, area_clicked.get(),
                                        city_clicked.get())

        if result == 1:
            msg = "Area updated succesfully"

        if len(msg) != 0:
            showinfo(
                title="Success",
                message=msg
            )
            delivery_person_homepage(user, root, db)
            return

        msg = "There is some error while updating address."
        showinfo(
            title="Error",
            message=msg
        )

    register_button = Button(frame, text="Update city", command=register_clicked, font=("Ariel 12 bold"))
    register_button.place(x=150, y=180, height=40, width=150)

    cancel_button = Button(root, text="Cancel", command=lambda: delivery_person_homepage(user,root,db), font = ("Ariel 15 bold"))
    cancel_button.place(x = 700,y = 80)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=700, y=20)

    root.mainloop()

def delivery_person_homepage(user, parent_window=None, db=None, page_number = 0):
    if db == None:
        db = DataBase()

    details = db.get_user_details(user.email)
    user = User(user.email, details[0], details[1], details[2], details[3])
    areaid = user.area_id

    if (parent_window != None):
        parent_window.destroy()

    root = tk.Tk()
    root.title('Deliver an order')

    if (areaid == None):
        add_city(user, root, db)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6 * screen_width) // 7
    window_height = (6 * screen_height) // 7

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/del.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    profile_button = Button(root, text="Edit city", command=lambda: add_city(user, root, db),
                            font=("Ariel 15 bold"))
    profile_button.place(x=24* window_width // 30, y=3*window_height // 20, height=window_height // 15,
                         width=1 * window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    my_orders_button = Button(root, text="My orders", command=lambda:my_orders_page(user, root, db), font=("Ariel 15 bold"))
    my_orders_button.place(x=24 * window_width // 30, y=5*window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    city = db.city_by_areaid(areaid)
    data = db.get_orders_for_delivery_by_city(city)

    orders = []
    for x in data:

        food_items = []
        food_ids = convert_string_to_food_ids(x[1])
        for y in food_ids:
            f = db.get_food_item_by_id(y)
            food_items.append(FoodItem(f[0], f[1], f[2], f[3], f[5], convert_string_to_bool(f[4])))

        orders.append(Order(x[0], food_items, x[2], x[3], x[4], x[5]))


    if len(orders) == 0:
        no_label = Label(root, text="Currently no orders to pick up in your city", font=("Goudy old style", 18, "bold"), fg="grey", bg="white")
        no_label.place(x = window_width//2-200,y = 50)

    num_pages = (len(orders)+5)//6

    for j in range(6*page_number, min(6*page_number+6, len(orders))):
        i = j-(6*page_number)
        xval = 30 + (i % 3)*350
        yval = 50 + (i // 3)*320
        new_frame = Frame(root, bg="white")
        new_frame.place(x=xval, y=yval, height=270, width=300)

        entry_frame = Frame(new_frame, bg="white")
        entry_frame.place(x=0, y=0, height=210, width=300)

        pickup_area_id = db.get_areaid_by_restaurant_id(orders[j].food_items[0].restaurant_id)
        delivery_area_id = db.get_areaid_by_user_email(orders[j].customer_email)

        name_label = Label(entry_frame, text="Restaurant \nname: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        name_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        name_value.insert('1.0', db.get_restaurant_name_from_id(orders[j].food_items[0].restaurant_id))
        name_value['state'] = 'disabled'
        pickup_label = Label(entry_frame, text="Pickup \narea: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        pickup_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        pickup_value.insert('1.0', db.get_area_by_areaid(pickup_area_id))
        pickup_value['state'] = 'disabled'
        delivery_label = Label(entry_frame, text="Delivery \narea: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        delivery_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        delivery_value.insert('1.0', db.get_area_by_areaid(delivery_area_id))
        delivery_value['state'] = 'disabled'
        name_label.place(x=10, y=30)
        name_value.place(x=110, y=30, width=180)
        pickup_label.place(x=10, y=90)
        pickup_value.place(x=110, y=90, width=180)
        delivery_label.place(x=10, y=150)
        delivery_value.place(x=110, y=150, width=180)

        def pickup_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            answer = askyesno(
                title='Confirmation',
                message='Are you sure that you want to deliver this order?'
            )
            if answer:
                db.set_delivery_person(orders[ind].order_id,user.email)
                delivery_person_homepage(user, root, db)

        pickup_button = Button(new_frame, text="Take Up", command=pickup_clicked, font=("Ariel 15 bold"))
        pickup_button.place(x=55, y=215, height=50,
                                width=200)


    def page_clicked():
        x = root.winfo_pointerx()
        ind = ((x-window_width//2+100)+70)//60
        ind -= 3
        cart_page(user, root, db, ind)

    if num_pages > 1:
        for i in range(num_pages):
            color = "white"
            if i == page_number:
                color = "grey"
            button = Button(root, text=str(i+1), command=page_clicked, font=("Ariel 15 bold"), bg = color)
            button.place(x=window_width//2+i*60-100, y=window_height-70, height=30, width=50)


    root.mainloop()

def my_orders_page(user, parent_window, db, page_number = 0):
    if db == None:
        db = DataBase()

    details = db.get_user_details(user.email)
    user = User(user.email, details[0], details[1], details[2], details[3])
    areaid = user.area_id

    if (parent_window != None):
        parent_window.destroy()

    root = tk.Tk()
    root.title('My orders')

    if (areaid == None):
        add_city(user, root, db)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6 * screen_width) // 7
    window_height = (6 * screen_height) // 7

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/del.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    profile_button = Button(root, text="Edit city", command=lambda: add_city(user, root, db),
                            font=("Ariel 15 bold"))
    profile_button.place(x=24* window_width // 30, y=3*window_height // 20, height=window_height // 15,
                         width=1 * window_width // 5 - 35)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    back_button = Button(root, text="Go Back", command=lambda: delivery_person_homepage(user, root, db),
                              font=("Ariel 15 bold"))
    back_button.place(x=24 * window_width // 30, y=5 * window_height // 20, height=window_height // 15,
                           width=1 * window_width // 5 - 35)

    city = db.city_by_areaid(areaid)
    data = db.get_orders_by_delivery_email(user.email)

    orders = []
    for x in data:

        food_items = []
        food_ids = convert_string_to_food_ids(x[1])
        for y in food_ids:
            f = db.get_food_item_by_id(y)
            food_items.append(FoodItem(f[0], f[1], f[2], f[3], f[5], convert_string_to_bool(f[4])))

        orders.append(Order(x[0], food_items, x[2], x[3], x[4], x[5]))


    if len(orders) == 0:
        no_label = Label(root, text="You have not picked up any orders", font=("Goudy old style", 18, "bold"), fg="grey", bg="white")
        no_label.place(x = window_width//2-200, y=50)

    num_pages = (len(orders)+5)//6

    for j in range(6*page_number, min(6*page_number+6, len(orders))):
        i = j-(6*page_number)
        xval = 30 + (i % 3)*350
        yval = 50 + (i // 3)*320
        new_frame = Frame(root, bg="white")
        new_frame.place(x=xval, y=yval, height=270, width=300)

        entry_frame = Frame(new_frame, bg="white")
        entry_frame.place(x=0, y=0, height=150, width=300)

        pickup_area_id = db.get_areaid_by_restaurant_id(orders[j].food_items[0].restaurant_id)
        delivery_area_id = db.get_areaid_by_user_email(orders[j].customer_email)

        name_label = Label(entry_frame, text="Restaurant: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        name_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        name_value.insert('1.0', db.get_restaurant_name_from_id(orders[j].food_items[0].restaurant_id))
        name_value['state'] = 'disabled'
        pickup_label = Label(entry_frame, text="Pickup: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        pickup_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        pickup_value.insert('1.0', db.get_area_by_areaid(pickup_area_id))
        pickup_value['state'] = 'disabled'
        delivery_label = Label(entry_frame, text="Delivery: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        delivery_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        delivery_value.insert('1.0', db.get_area_by_areaid(delivery_area_id))
        delivery_value['state'] = 'disabled'
        status_label = Label(entry_frame, text="Pickup: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        status_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        status_value.insert('1.0', orders[j].status)
        status_value['state'] = 'disabled'
        name_label.place(x=10, y=30)
        name_value.place(x=110, y=30, width=180)
        pickup_label.place(x=10, y=60)
        pickup_value.place(x=110, y=60, width=180)
        delivery_label.place(x=10, y=90)
        delivery_value.place(x=110, y=90, width=180)
        status_label.place(x=10, y=120)
        status_value.place(x=110, y=120, width=180)

        stats = ["Being Prepared", "On the way", "Delivered"]

        def pickup_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            answer = askyesno(
                title='Confirmation',
                message='Are you sure that you want to deliver this order?'
            )
            if answer:
                db.set_delivery_person(orders[ind].order_id,user.email)
                delivery_person_homepage(user, root, db)

        def more_info_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            msg = ""
            price = 0
            for x in orders[ind].food_items:
                price += x.price
            msg += "Email: "+orders[ind].customer_email + '\n'
            msg += "Pickup Address: " + db.get_address_by_restaurant_id(orders[ind].food_items[0].restaurant_id) + '\n'
            msg += "Delivery Address: "+ db.get_address_by_email(orders[ind].customer_email) + '\n'
            msg += "Price: " + str(price)

            showinfo(
                title='Information',
                message=msg
            )

        def update_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            curstatus = orders[ind].status
            newstatus = ""
            if curstatus == stats[0]:
                newstatus = stats[1]
            if curstatus == stats[1]:
                newstatus = stats[2]
            answer = askyesno(
                title = 'confirmation',
                message = 'Are you sure that you want to update the status from {0} to {1}?'.format(curstatus, newstatus)
            )
            if answer:
                db.update_status(orders[ind].order_id, newstatus)
                my_orders_page(user, root, db)

        more_info_button = Button(new_frame, text="More Info", command=more_info_clicked, font=("Ariel 15 bold"))
        more_info_button.place(x=50, y=165, height=40,
                                width=200)

        update_button = Button(new_frame, text="Update status", command=update_clicked, font=("Ariel 15 bold"))
        if orders[j].status != 'Delivered':
            update_button.place(x=50, y=210, height=40,
                                width=200)


    def page_clicked():
        x = root.winfo_pointerx()
        ind = ((x-window_width//2+100)+70)//60
        ind -= 3
        cart_page(user, root, db, ind)

    if num_pages > 1:
        for i in range(num_pages):
            color = "white"
            if i == page_number:
                color = "grey"
            button = Button(root, text=str(i+1), command=page_clicked, font=("Ariel 15 bold"), bg = color)
            button.place(x=window_width//2+i*60-100, y=window_height-70, height=30, width=50)


    root.mainloop()

def my_orders_customer(user, parent_window = None, db = None, page_number = 0):
    if db == None:
        db = DataBase()

    details = db.get_user_details(user.email)
    user = User(user.email, details[0], details[1], details[2], details[3])
    areaid = user.area_id

    if (parent_window != None):
        parent_window.destroy()

    root = tk.Tk()
    root.title('My orders')

    if (areaid == None):
        add_city(user, root, db)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = (6 * screen_width) // 7
    window_height = (6 * screen_height) // 7

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.iconbitmap('Images/logo.ico')
    root.resizable(False, False)
    background_image = ImageTk.PhotoImage(
        Image.open('Images/del.jpg').resize((window_width + 100, window_height), Image.ANTIALIAS))
    background_image_label = tk.Label(root, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)

    logout_button = Button(root, text="Logout", command=lambda: login_page(root, db), font=("Ariel 15 bold"))
    logout_button.place(x=24 * window_width // 30, y=window_height // 20, height=window_height // 15,
                        width=1 * window_width // 5 - 35)

    back_button = Button(root, text="Go Back", command=lambda: customer_home_page(user, root, db),
                              font=("Ariel 15 bold"))
    back_button.place(x=24 * window_width // 30, y=3 * window_height // 20, height=window_height // 15,
                           width=1 * window_width // 5 - 35)

    data = db.get_orders_by_user_email(user.email)

    orders = []
    for x in data:

        food_items = []
        food_ids = convert_string_to_food_ids(x[1])
        for y in food_ids:
            f = db.get_food_item_by_id(y)
            food_items.append(FoodItem(f[0], f[1], f[2], f[3], f[5], convert_string_to_bool(f[4])))

        orders.append(Order(x[0], food_items, x[2], x[3], x[4], x[5]))


    if len(orders) == 0:
        no_label = Label(root, text="You have not placed any orders till now", font=("Goudy old style", 18, "bold"), fg="grey", bg="white")
        no_label.place(x = window_width//2-200, y=50)

    num_pages = (len(orders)+5)//6

    for j in range(6*page_number, min(6*page_number+6, len(orders))):
        i = j-(6*page_number)
        xval = 30 + (i % 3)*350
        yval = 50 + (i // 3)*320
        new_frame = Frame(root, bg="white")
        new_frame.place(x=xval, y=yval, height=270, width=300)

        entry_frame = Frame(new_frame, bg="white")
        entry_frame.place(x=0, y=0, height=190, width=300)

        pickup_area_id = db.get_areaid_by_restaurant_id(orders[j].food_items[0].restaurant_id)
        delivery_area_id = db.get_areaid_by_user_email(orders[j].customer_email)

        name_label = Label(entry_frame, text="Restaurant: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        name_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        name_value.insert('1.0', db.get_restaurant_name_from_id(orders[j].food_items[0].restaurant_id))
        name_value['state'] = 'disabled'
        pickup_label = Label(entry_frame, text="Pickup: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        pickup_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        pickup_value.insert('1.0', db.get_area_by_areaid(pickup_area_id))
        pickup_value['state'] = 'disabled'
        delivery_label = Label(entry_frame, text="Delivery: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        delivery_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        delivery_value.insert('1.0', db.get_area_by_areaid(delivery_area_id))
        delivery_value['state'] = 'disabled'
        status_label = Label(entry_frame, text="Pickup: ", font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        status_value = Text(entry_frame, font=("Goudy old style", 14, "bold"), fg="grey", bg="white")
        status_value.insert('1.0', orders[j].status)
        status_value['state'] = 'disabled'
        name_label.place(x=10, y=30)
        name_value.place(x=110, y=30, width=180)
        pickup_label.place(x=10, y=70)
        pickup_value.place(x=110, y=70, width=180)
        delivery_label.place(x=10, y=110)
        delivery_value.place(x=110, y=110, width=180)
        status_label.place(x=10, y=150)
        status_value.place(x=110, y=150, width=180)

        stats = ["Being Prepared", "On the way", "Delivered"]

        def pickup_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            answer = askyesno(
                title='Confirmation',
                message='Are you sure that you want to deliver this order?'
            )
            if answer:
                db.set_delivery_person(orders[ind].order_id,user.email)
                delivery_person_homepage(user, root, db)

        def more_info_clicked():
            x = root.winfo_pointerx()
            y = root.winfo_pointery()
            ind = 6 * page_number
            if y > 500:
                ind += 3
            if x > 730:
                ind += 2
            elif x > 380:
                ind += 1
            msg = ""
            price = 0
            for x in orders[ind].food_items:
                price += x.price
            de = "Not assigned"
            if orders[ind].delivery_person_email != None:
                de = orders[ind].delivery_person_email
            msg += "Delivery boy email: "+ de + '\n'
            msg += "Pickup Address: " + db.get_address_by_restaurant_id(orders[ind].food_items[0].restaurant_id) + '\n'
            msg += "Delivery Address: "+ db.get_address_by_email(orders[ind].customer_email) + '\n'
            msg += "Price: " + str(price)

            showinfo(
                title='Information',
                message=msg
            )

        more_info_button = Button(new_frame, text="More Info", command=more_info_clicked, font=("Ariel 15 bold"))
        more_info_button.place(x=50, y=210, height=50,
                                width=200)


    def page_clicked():
        x = root.winfo_pointerx()
        ind = ((x-window_width//2+100)+70)//60
        ind -= 3
        cart_page(user, root, db, ind)

    if num_pages > 1:
        for i in range(num_pages):
            color = "white"
            if i == page_number:
                color = "grey"
            button = Button(root, text=str(i+1), command=page_clicked, font=("Ariel 15 bold"), bg = color)
            button.place(x=window_width//2+i*60-100, y=window_height-70, height=30, width=50)


    root.mainloop()