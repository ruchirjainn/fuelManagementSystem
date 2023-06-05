# ***************CODE BY RUCHIR JAIN**********************
from tkinter import *
from PIL import Image, ImageTk
from register import RegisterCustomer
from inventory import Inventory
from report import Report
from buying import Buying


class FuelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Management System")
        self.root.geometry("1550x800+0+0")

        # **********1st Image****************
        img1 = Image.open(r"D:\pythonProjects\Fuel Management System\Image\poster.jpg")
        img1 = img1.resize((1550, 146), Image.ANTIALIAS)  # antialias convert to low resolution
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=146)

        # **********Logo****************
        img2 = Image.open(r"D:\pythonProjects\Fuel Management System\Image\logo2.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)  # antialias convert to low resolution
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # **************Main Frame**********
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=140, width=1550, height=700)

        # **********Menu*************
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4,
                         relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # **********Button menu list*********
        button_frame = Frame(main_frame, bd=4, relief=RIDGE)
        button_frame.place(x=0, y=35, width=228, height=190)

        register_button = Button(button_frame, command=self.register, text="REGISTER", width=22,
                                 font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,
                                 cursor="hand1")
        register_button.grid(row=0, column=0, pady=1)

        buy_button = Button(button_frame, command=self.buying, text="BUYING", width=22,
                            font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,
                            cursor="hand1")
        buy_button.grid(row=1, column=0, pady=1)

        inventory_button = Button(button_frame, command=self.inventory, text="INVENTORY", width=22,
                                  font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,
                                  cursor="hand1")
        inventory_button.grid(row=2, column=0, pady=1)

        report_btn = Button(button_frame, command=self.report, text="REPORT", width=22,
                            font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, relief=RIDGE, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(button_frame, command=self.logout, text="LOGOUT", width=22,
                            font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,
                            cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # ************Right Side Image**********
        img3 = Image.open(r"D:\pythonProjects\Fuel Management System\Image\banner.jpg")
        img3 = img3.resize((1310, 627))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=230, y=0, width=1310, height=627)

        # *************Down Image************
        img4 = Image.open(r"D:\pythonProjects\Fuel Management System\Image\pump.jpg")
        img4 = img4.resize((230, 400), Image.ANTIALIAS)  # antialias convert to low resolution
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=225, width=230, height=400)

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = RegisterCustomer(self.new_window)

    def inventory(self):
        self.new_window = Toplevel(self.root)
        self.app = Inventory(self.new_window)

    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)

    def buying(self):
        self.new_window = Toplevel(self.root)
        self.app = Buying(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    obj = FuelManagementSystem(root)
    root.mainloop()
