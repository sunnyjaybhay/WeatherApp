from tkinter import *
from tkinter import messagebox
from api import api
from DataBase import DB

class WetherApplication:
    def __init__(self):


        self.dbo = DB()
        self.apio = api()

        self.root = Tk()

        self.root.geometry("1920x1080")
        self.root.configure(bg="#000000")
        self.root.title("Weather Application")

        # Load background image
        self.background_image = PhotoImage(file=r"D:\Projects\WeatherApp\image\3.png")
        self.background_label = Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
        self.login()
        #self.clear()
        self.root.mainloop() # to hold your output window


    def clear(self):
        for i in self.root.slaves():
            i.destroy()
            #print(i)


    def login(self):
        self.clear()

        heading = Label(self.root, text="Welcome to my Weather Application", bg="#000000", fg="white")
        heading.config(font=("Cambria",32,"italic","bold"))
        heading.pack(pady=(100,75))

        email_label = Label(self.root, text="Enter your Email", bg="#000000", fg="white")
        email_label.config(font=("Cambria", 16, "bold"))
        #email_label.place(x=520, y=180)  # Adjust x and y values as needed
        email_label.pack(pady=(5,5))

        self.email_input = Entry(self.root, width=25)
        self.email_input.config(font=("Cambria", 16))
        #self.email_input.place(x=450, y=210)
        self.email_input.pack(pady=(5, 25), ipady=1)


        password_label = Label(self.root, text="Enter your password", bg="#000000", fg="white")
        password_label.config(font=("Cambria", 16, "bold"))
        #password_label.place(x=500, y=240)
        password_label.pack(pady=(5, 5))

        self.password_input = Entry(self.root, width=25, show="*")
        self.password_input.config(font=("Cambria", 16))
        self.password_input.pack(pady=(5, 50), ipady=1)
        #self.password_input.place(x=450, y=270)

        login_btn = Button(self.root, text="Login", width=5,command=self.perform_login)
        login_btn.config(font=("Cambria", 15))
        #login_btn.place(x=570, y=320)
        login_btn.pack(pady=(5, 20))


        member_label =Label(self.root,text="Not a member...?", bg="#000000", fg="white")
        member_label.config(font=("Cambria",12))
        #member_label.place(x=540, y=360)
        member_label.pack(pady=(10,0))

        register_btn = Button(self.root, text="Register here...", bg="white", fg="black",command=self.register)
        register_btn.config(font=("Cambria", 10))
        #register_btn.place(x=555, y=390)
        register_btn.pack(pady=(0, 0))


    def register(self):
        self.clear()

        heading = Label(self.root, text="Register", bg="#000000", fg="white")
        heading.config(font=("Cambria", 24, "italic", "bold"))
        heading.pack(pady=(50, 75))

        username_label = Label(self.root, text="Enter your Username", bg="#000000", fg="white")
        username_label.config(font=("Cambria", 16, "bold"))
        username_label.pack(pady=(5, 5))
        self.username_input = Entry(self.root, width=25)
        self.username_input.config(font=("Cambria", 16))
        self.username_input.pack(pady=(5, 25), ipady=1)

        email_label = Label(self.root, text="Enter your Email", bg="#000000", fg="white")
        email_label.config(font=("Cambria", 16, "bold"))
        email_label.pack(pady=(5, 5))
        self.email_input = Entry(self.root, width=25)
        self.email_input.config(font=("Cambria", 16))
        self.email_input.pack(pady=(5, 25), ipady=1)

        password_label = Label(self.root, text="Enter your Password", bg="#000000", fg="white")
        password_label.config(font=("Cambria", 16, "bold"))
        password_label.pack(pady=(5, 5))
        self.password_input = Entry(self.root, width=25,show="*")
        self.password_input.config(font=("Cambria", 16))
        self.password_input.pack(pady=(5, 25), ipady=1)


        register_btn = Button(self.root, text="Register", width=10, command=self.perform_registration)
        register_btn.config(font=("Cambrian",16))
        register_btn.pack(pady=(5,5))

        member_label = Label(self.root, text="Already a member...?", bg="#000000",fg="White")
        member_label.config(font=("Cambria",12))
        member_label.pack(pady=(10,0))

        login_btn = Button(self.root, text="Login", width=10,command=self.login)
        login_btn.config(font=("Cambrian", 16))
        login_btn.pack(pady=(0,0))



    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.check_login(email,password)

        if response == 1:
            messagebox.showinfo("Success","Login Succussfully")
            self.home()


        elif response == 0:
            messagebox.showerror("Failed","Incorrect Password")
            self.login()

        else:
            messagebox.showwarning("Failed","Email not Registered")
            self.register()



    def perform_registration(self):
        username = self.username_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.register_user(username,email,password)

        if response == 0:
            messagebox.showwarning("Failed","Email already registered")
            self.login()

        else:
            messagebox.showinfo("Succeful","Email registered")
            self.login()



    def home(self):
        self.clear()

        heading = Label(self.root, text="Weather Application", bg="#000000", fg="white")
        heading.config(font=("Cambria", 24, "bold"))
        heading.pack(pady=(50, 75))

        search_by_city_btn = Button(self.root, text="Search by city name", width=20, height=2, command=self.using_city_name)
        search_by_city_btn.config(font=("Cambria", 18))
        #search_by_city_btn.place(x=480, y=180)  # Adjust x and y values as needed
        search_by_city_btn.pack(pady=(5, 5))

        search_by_coordinates_btn = Button(self.root, text="Search by Coodinates", width=20,height=2, command=self.using_coordinates)
        search_by_coordinates_btn.config(font=("Cambria", 18))
        #search_by_coordinates_btn.place(x=480, y=280)  # Adjust x and y values as needed
        search_by_coordinates_btn.pack(pady=(50, 50))

        logout_btn = Button(self.root, text="Logout", width=10,height=2, command= self.login)
        logout_btn.config(font=("Cambria", 12))
        #logout_btn.place(x=570, y=380)  # Adjust x and y values as needed
        logout_btn.pack(pady=(25, 5))


    def using_city_name(self):
        self.clear()

        heading = Label(self.root, text="Weather Application", bg="#000000", fg="white")
        heading.config(font=("Cambria", 24, "bold"))
        heading.pack(pady=(25, 5))

        city_label = Label(self.root, text="Enter city name", bg="#000000", fg="white")
        city_label.config(font=("Cambria", 18))
        city_label.pack(pady=(5, 5))
        #city_label.place(x=520, y=180)


        self.city_input = Entry(self.root, width=25)
        self.city_input.config(font=("Cambria", 16))
        #self.city_input.place(x=450, y=220)
        self.city_input.pack(pady=(5, 5), ipady=1)


        search_by_city_btn = Button(self.root, text="Search", width=10, command = self.display_info)
        search_by_city_btn.config(font=("Cambria", 18))
        #search_by_city_btn.place(x=530, y=260)
        search_by_city_btn.pack(pady=(5, 25))

        self.result = Label(self.root, text="", bg="#000000", fg="white")
        self.result.config(font=("Cambria", 18))
        self.result.pack(pady=(5, 5))


        # back btn
        back_btn = Button(self.root, text="back", width=10, command= self.home)
        back_btn.config(font=("Cambria", 18))
        #back_btn.place(x=530, y=320)
        back_btn.pack(pady=(5, 25))

        self.result = Label(self.root, text="", bg="#000000", fg="white")
        self.result.config(font=("Cambria", 18))
        self.result.pack(pady=(5, 5))



    def using_coordinates(self):
        self.clear()

        heading = Label(self.root, text="Weather Application", bg="#000000", fg="white")
        heading.config(font=("Cambria", 24, "bold"))
        heading.pack(pady=(25, 5))

        city_label = Label(self.root, text="Enter Coordinates", bg="#000000", fg="white")
        city_label.config(font=("Cambria", 18))
        #city_label.place(x=500, y=180)
        city_label.pack(pady=(5, 5))

        self.city_input = Entry(self.root, width=25)
        self.city_input.config(font=("Cambria", 16))
        #self.city_input.place(x=450, y=220)
        self.city_input.pack(pady=(5, 5), ipady=1)


        search_by_city_btn = Button(self.root, text="Search", width=10, command = self.display_info)
        search_by_city_btn.config(font=("Cambria", 18))
        #search_by_city_btn.place(x=530, y=260)
        search_by_city_btn.pack(pady=(5, 25))

        self.result = Label(self.root, text="", bg="#000000", fg="white")
        self.result.config(font=("Cambria", 18))
        #self.result.place(x=530, y=260)
        self.result.pack(pady=(5, 5))

        # back btn
        back_btn = Button(self.root, text="back", width=10, command=self.home)
        back_btn.config(font=("Cambria", 18))
        #back_btn.place(x=530, y=320)
        back_btn.pack(pady=(5, 25))

        self.result = Label(self.root, text="", bg="#000000", fg="white")
        self.result.config(font=("Cambria", 18))
        self.result.pack(pady=(5, 5))



    def display_info(self):

        city = self.city_input.get()
        data = self.apio.get_info_by_city_name(city)

        if data == 0:
            self.result['text'] = "City not found"
        else:
            txt = ""
            for i in data:
                txt += str(i) + " -> " + str(data[i]) + "\n\n"
            self.result['text'] = txt








object = WetherApplication()