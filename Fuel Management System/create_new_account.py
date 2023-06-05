# ***************CODE BY RUCHIR JAIN**********************
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class CreateNewAccount:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Management System")
        self.root.geometry("1550x800+0+0")

        # *********Variables*************
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_question = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_checkbutton = IntVar()

        # ********Background Image***********
        img1 = Image.open(r"D:\pythonProjects\Fuel Management System\Image\banner3")
        self.photoImg1 = ImageTk.PhotoImage(img1)
        labelImg1 = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        labelImg1.place(x=0, y=0, relwidth=1, relheight=1)

        # ********Left Side Image***********
        img2 = Image.open(r"D:\pythonProjects\Fuel Management System\Image\pump.jpg")
        img2=img2.resize((460,540),Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        labelImg2 = Label(self.root, image=self.photoImg2, bd=4, relief=RIDGE)
        labelImg2.place(x=50, y=100, width=470, height=550)

        # ***********Frame*************
        register_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        register_frame.place(x=520, y=100, width=800, height=550)

        # **********Frame Vairables***********
        register_label = Label(register_frame, text="REGISTER HERE", font=("times new roman", 20, "bold"),
                               fg="dark green", bg="white")
        register_label.place(x=20, y=20)

        # *********** Labels & entries**********

        # *********1st row************
        label_fname = Label(register_frame, text="First Name", font=("times new roman", 16, "bold"), bg="white")
        label_fname.place(x=20, y=100)
        self.entry_fname = ttk.Entry(register_frame, textvariable=self.var_fname, font=("arial", 13, "bold"))
        self.entry_fname.place(x=20, y=130, width=250)

        label_lname = Label(register_frame, text="Last Name", font=("times new roman", 16, "bold"), bg="white")
        label_lname.place(x=370, y=100)
        self.entry_lname = ttk.Entry(register_frame, textvariable=self.var_lname, font=("arial", 13, "bold"))
        self.entry_lname.place(x=370, y=130, width=250)

        # *********2nd row************
        label_contact = Label(register_frame, text="Contact Number", font=("times new roman", 16, "bold"), bg="white")
        label_contact.place(x=20, y=170)
        self.entry_contact = ttk.Entry(register_frame, textvariable=self.var_contact, font=("arial", 13, "bold"))
        self.entry_contact.place(x=20, y=200, width=250)

        label_email = Label(register_frame, text="Email", font=("times new roman", 16, "bold"), bg="white")
        label_email.place(x=370, y=170)
        self.entry_email = ttk.Entry(register_frame, textvariable=self.var_email, font=("arial", 13, "bold"))
        self.entry_email.place(x=370, y=200, width=250)

        # *********3rd row************
        label_quesion = Label(register_frame, text="Select Security Questions", font=("times new roman", 15, "bold"),
                              fg="black", bg="white")
        label_quesion.place(x=20, y=240)
        combo_question = ttk.Combobox(register_frame, textvariable=self.var_question, font=("arial", 12, "bold"),
                                      width=26, state="readonly")
        combo_question["values"] = ("Select", "Birth Place", "Favorite Food", "Mother Name")
        combo_question.current(0)
        combo_question.place(x=20, y=270, width=250)

        label_answer = Label(register_frame, text="Security Answer", font=("times new roman", 16, "bold"), bg="white")
        label_answer.place(x=370, y=240)
        self.entry_answer = ttk.Entry(register_frame, textvariable=self.var_answer, font=("arial", 13, "bold"))
        self.entry_answer.place(x=370, y=270, width=250)

        # *********4th row************
        label_password = Label(register_frame, text="Password", font=("times new roman", 16, "bold"), bg="white")
        label_password.place(x=20, y=310)
        self.entry_password = ttk.Entry(register_frame, textvariable=self.var_password, font=("arial", 13, "bold"))
        self.entry_password.place(x=20, y=340, width=250)

        label_confirm_password = Label(register_frame, text="Confirm Password", font=("times new roman", 16, "bold"),
                                       bg="white")
        label_confirm_password.place(x=370, y=310)
        self.entry_confirm_password = ttk.Entry(register_frame, textvariable=self.var_confirm_password,
                                                font=("arial", 13, "bold"))
        self.entry_confirm_password.place(x=370, y=340, width=250)

        checkbox = Checkbutton(register_frame, variable=self.var_checkbutton, bg="white", onvalue=1, offvalue=0)
        checkbox.place(x=20, y=390)
        label_agreement = Label(register_frame, text="I agree with the Terms & Conditions",
                                font=("times new roman", 13, "bold"), bg="white")
        label_agreement.place(x=40, y=390)

        # *********Register & Login Button*********
        img3 = Image.open(r"D:\pythonProjects\Fuel Management System\images\hotel images\register-now-button1.jpg")
        img3 = img3.resize((200, 50), Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        button_register = Button(register_frame, command=self.register_data, image=self.photoImg3, bg="white",
                                 borderwidth=0, activebackground="white", cursor="hand2")
        button_register.place(x=50, y=420, width=200)

        img4 = Image.open(r"D:\pythonProjects\Fuel Management System\images\hotel images\loginpng.png")
        img4 = img4.resize((150, 40), Image.LANCZOS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        button_login = Button(register_frame, command=self.go_to_login_page, image=self.photoImg4, bg="white",
                              borderwidth=0, activebackground="white",
                              cursor="hand2")
        button_login.place(x=300, y=425, width=200)

    # ***********Function Declaration************

    def register_data(self):
        if self.var_fname.get() == "" or self.var_checkbutton.get() == "" or self.var_email.get() == "" or self.var_question.get() == "Select":
            messagebox.showerror(title="Error", message="All Entries are required",parent=self.root)
        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror(title="Error", message="Password & Confirm Password are'nt matching",parent=self.root)
        elif self.var_checkbutton.get() == 0:
            messagebox.showerror(title="Error", message="Please agree with the terms & condition",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                           database="fuel management system")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(title="Error", message="User already exist,Please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_question.get(),
                    self.var_answer.get(),
                    self.var_password.get(),
                ))
                messagebox.showinfo(title="Error", message="Created User Successfully",parent=self.root)
            conn.commit()
            conn.close()

    def go_to_login_page(self):
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    obj = CreateNewAccount(root)
    root.mainloop()
