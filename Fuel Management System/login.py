# ***************CODE BY RUCHIR JAIN**********************
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from create_new_account import CreateNewAccount
import mysql.connector
from main import FuelManagementSystem


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Management System")
        self.root.geometry("1550x800+0+0")

        # ******************Variables************
        self.var_security_question = StringVar()
        self.var_security_answer = StringVar()
        self.var_new_password = StringVar()

        # *********Background Wallpaper********
        img1 = Image.open(r"D:\pythonProjects\Fuel Management System\Image\banner.jpg")
        img1=img1.resize((2550,800),Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        labelImg1 = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        labelImg1.place(x=0, y=0, relwidth=1, relheight=1)

        # *********Login Page Frame***********
        login_frame = Frame(self.root, bd=4, relief=RIDGE, bg="black")
        login_frame.place(x=610, y=170, width=340, height=450)

        # ********Login Frame Variables,Buttons,Icons********
        img2 = Image.open(r"D:\pythonProjects\Fuel Management System\images\hotel images\LoginIconAppl.png")
        img2 = img2.resize((100, 100), Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        labelImg2 = Label(self.root, image=self.photoImg2, bd=4, relief=RIDGE, borderwidth=0, bg="black")
        labelImg2.place(x=730, y=175, width=100, height=100)

        get_started = Label(login_frame, text="  Welcome ", font=("times new roman", 20, "bold"), fg="white",
                            bg="black")
        get_started.place(x=95, y=100)

        img3 = Image.open(r"D:\pythonProjects\Fuel Management System\images\hotel images\LoginIconAppl.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        labelImg3 = Label(self.root, image=self.photoImg3, bd=4, relief=RIDGE, borderwidth=0, bg="black")
        labelImg3.place(x=653, y=324, width=25, height=25)

        label_username = Label(login_frame, text="Username", font=("times new roman", 15, "bold"), fg="white",
                               bg="black")
        label_username.place(x=70, y=150)
        self.entry_username = ttk.Entry(login_frame, font=("arial", 13, "bold"))
        self.entry_username.place(x=40, y=180, width=270)

        img4 = Image.open(r"D:\pythonProjects\Fuel Management System\images\hotel images\lock-512.png")
        img4 = img4.resize((25, 25), Image.LANCZOS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        labelImg4 = Label(self.root, image=self.photoImg4, bd=4, relief=RIDGE, borderwidth=0, bg="black")
        labelImg4.place(x=653, y=395, width=25, height=25)

        label_password = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), fg="white",
                               bg="black")
        label_password.place(x=70, y=220)
        self.entry_password = ttk.Entry(login_frame, font=("arial", 13, "bold"))
        self.entry_password.place(x=40, y=250, width=270)

        # *******Login Button***********
        button_login = Button(login_frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                              relief=RIDGE,
                              fg="white", bg="red", activeforeground="white", activebackground="red")
        button_login.place(x=110, y=300, width=120, height=35)

        # ********Create User & forgot password button*******
        button_register = Button(login_frame, command=self.create_new_user, text="Create New User ",
                                 font=("times new roman", 10, "bold"),
                                 borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white",
                                 activebackground="black")
        button_register.place(x=10, y=350, width=160)

        button_forgot_password = Button(login_frame, command=self.forgot_password, text="Forgot Password?",
                                        font=("times new roman", 10, "bold"),
                                        borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white",
                                        activebackground="black")
        button_forgot_password.place(x=10, y=380, width=160)

    # ********Actual Logic************
    def login(self):
        if self.entry_username.get() == "" or self.entry_password.get() == "":
            messagebox.showerror(title="Error", message="All fields required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                           database="fuel management system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.entry_username.get(), self.entry_password.get()))
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror(title="Error", message="Invalid username & password")
            else:
                self.new_window = Toplevel(self.root)
                self.app = FuelManagementSystem(self.new_window)
            conn.commit()
            conn.close()

    def create_new_user(self):
        self.new_window = Toplevel(self.root)
        self.app = CreateNewAccount(self.new_window)

    # ***********************Reset password*************************
    def reset_password(self):
        if self.var_security_question.get()=="Select" or self.var_security_answer.get()=="" or self.var_new_password.get()=="":
            messagebox.showerror("Error","Enter the Valid Entries",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",database="fuel management system")
            my_cursor = conn.cursor()
            query=("select securityQ,securityA from register where email=%s")
            value=(self.entry_username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)
            if row[0]==self.var_security_question.get() and row[1]==self.var_security_answer.get():
                query=("update register set password=%s where email=%s")
                value=(self.var_new_password.get(),self.entry_username.get(),)
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo(title="Success",message="Password Successfully!",parent=self.root2)
                self.root2.destroy()
            else:
                messagebox.showerror(title="Error",message="Invalid Security Entries",parent=self.root2)


    # ***********************Forgot password*************************
    def forgot_password(self):
        if self.entry_username.get() == "":
            messagebox.showerror(title="Error", message="enter the username")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",database="fuel management system")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.entry_username.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror(title="Error", message="Email/Username Not found 404!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                self.root2.config(bg="black")

                label_forgot_password=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="black")
                label_forgot_password.place(x=0,y=10,relwidth=1)

                label_quesion = Label(self.root2, text="Select Security Questions",font=("times new roman", 15, "bold"),fg="white", bg="black")
                label_quesion.place(x=50, y=80)
                combo_question = ttk.Combobox(self.root2,textvariable=self.var_security_question,font=("arial", 12, "bold"),width=26, state="readonly")
                combo_question["values"] = ("Select", "Birth Place", "Favorite Food", "Mother Name")
                combo_question.current(0)
                combo_question.place(x=50, y=110, width=250)

                label_security_answer = Label(self.root2, text="Security Answer", font=("times new roman", 16, "bold"),bg="black",fg="white")
                label_security_answer.place(x=50, y=150)
                self.entry_security_answer = ttk.Entry(self.root2, textvariable=self.var_security_answer,font=("arial", 13, "bold"))
                self.entry_security_answer.place(x=50, y=180, width=250)

                label_new_password = Label(self.root2, text="New Password", font=("times new roman", 16, "bold"),bg="black",fg="white")
                label_new_password.place(x=50, y=220)
                self.entry_new_password = ttk.Entry(self.root2,textvariable=self.var_new_password, font=("arial", 13, "bold"))
                self.entry_new_password.place(x=50, y=250, width=250)

                button_reset = Button(self.root2,command=self.reset_password,text="RESET",fg="white", bg="green",borderwidth=0, activebackground="white",cursor="hand2")
                button_reset.place(x=100, y=300, width=150)

                self.root2.mainloop()


if __name__ == '__main__':
    root = Tk()
    obj = LoginPage(root)
    root.mainloop()
