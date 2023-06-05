# ***************CODE BY RUCHIR JAIN**********************
from random import random
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random


class Buying:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Management System")
        self.root.geometry("1295x700+230+170")

        # *********Variables************
        self.var_bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.var_bill_no.set(str(x))

        self.var_contact_number = StringVar()
        self.var_customer_name = StringVar()
        self.var_license_number = StringVar()
        self.var_model_number = StringVar()
        self.var_car_number = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_post_code = StringVar()
        self.var_fuel_type = StringVar()
        self.var_quantity = StringVar()
        self.var_check_availability = StringVar()

        self.var_latest_quantity = StringVar()

        self.var_search_bill_number = StringVar()

        # ******Label Frame***********
        labelFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelFrameLeft.place(x=0, y=0, width=425, height=610)

        # cust reference
        label_bill_no = Label(labelFrameLeft, text="Bill No:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_bill_no.grid(row=0, column=0, sticky=W)
        entry_bill_no = Entry(labelFrameLeft, textvariable=self.var_bill_no, width=28, font=("arial", 13),
                              state="readonly")
        entry_bill_no.grid(row=0, column=1)

        # customer contact number
        label_contact_number = Label(labelFrameLeft, text="Contact No:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_contact_number.grid(row=1, column=0, sticky=W)
        entry_contact_number = Entry(labelFrameLeft, textvariable=self.var_contact_number, width=23, font=("arial", 13))
        entry_contact_number.grid(row=1, column=1, sticky=W)

        # ***********Fetch Button***********
        button_fetch_data = Button(labelFrameLeft, command=self.fetch_data, text="Fetch Data",
                                   font=("arial", 11, "bold"), bg="black", fg="gold", width=9)
        button_fetch_data.place(x=325, y=41, height=26)

        # customer name
        label_customer_name = Label(labelFrameLeft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_name.grid(row=2, column=0, sticky=W)
        entry_customer_name = Entry(labelFrameLeft, textvariable=self.var_customer_name, width=28, font=("arial", 13),
                                    state="readonly")
        entry_customer_name.grid(row=2, column=1)

        # license number
        label_license_number = Label(labelFrameLeft, text="License Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_license_number.grid(row=3, column=0, sticky=W)
        entry_license_number = Entry(labelFrameLeft, textvariable=self.var_license_number, width=28, font=("arial", 13),
                                     state="readonly")
        entry_license_number.grid(row=3, column=1)

        # model number
        label_model_number = Label(labelFrameLeft, text="Model Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_model_number.grid(row=4, column=0, sticky=W)
        entry_model_number = Entry(labelFrameLeft, textvariable=self.var_model_number, width=28, font=("arial", 13),
                                   state="readonly")
        entry_model_number.grid(row=4, column=1)

        # car number
        label_car_number = Label(labelFrameLeft, text="Car Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_car_number.grid(row=5, column=0, sticky=W)
        entry_car_number = Entry(labelFrameLeft, textvariable=self.var_car_number, width=28, font=("arial", 13),
                                 state="readonly")
        entry_car_number.grid(row=5, column=1)

        # gender
        label_gender = Label(labelFrameLeft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=6, column=0, sticky=W)
        entry_gender = Entry(labelFrameLeft, textvariable=self.var_gender, width=28, font=("arial", 13),
                             state="readonly")
        entry_gender.grid(row=6, column=1)

        # email
        label_email = Label(labelFrameLeft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_email.grid(row=7, column=0, sticky=W)
        entry_email = Entry(labelFrameLeft, textvariable=self.var_email, width=28, font=("arial", 13), state="readonly")
        entry_email.grid(row=7, column=1)

        # state
        label_state = Label(labelFrameLeft, text="State:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_state.grid(row=8, column=0, sticky=W)
        entry_state = Entry(labelFrameLeft, textvariable=self.var_state, width=28, font=("arial", 13), state="readonly")
        entry_state.grid(row=8, column=1)

        # city
        label_city = Label(labelFrameLeft, text="City:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_city.grid(row=9, column=0, sticky=W)
        entry_city = Entry(labelFrameLeft, textvariable=self.var_city, width=28, font=("arial", 13), state="readonly")
        entry_city.grid(row=9, column=1)

        # postcode
        label_postcode = Label(labelFrameLeft, text="PostCode:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_postcode.grid(row=10, column=0, sticky=W)
        entry_postcode = Entry(labelFrameLeft, textvariable=self.var_post_code, width=28, font=("arial", 13),
                               state="readonly")
        entry_postcode.grid(row=10, column=1)

        # type of fuel
        label_email = Label(labelFrameLeft, text="Fuel Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_email.grid(row=11, column=0, sticky=W)
        combo_fuel_type = ttk.Combobox(labelFrameLeft, textvariable=self.var_fuel_type, font=("arial", 12), width=21,
                                       state="readonly")
        combo_fuel_type["values"] = ("PETROL", "CNG", "DIESEL")
        combo_fuel_type.current(0)
        combo_fuel_type.place(x=138, y=390, width=259, height=25)

        # quantity
        label_quantity = Label(labelFrameLeft, text="Quantity:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_quantity.grid(row=12, column=0, sticky=W)
        entry_quantity = Entry(labelFrameLeft, textvariable=self.var_quantity, width=28, font=("arial", 13))
        entry_quantity.place(x=138, y=425, width=80, height=25)
        label_quantity = Label(labelFrameLeft, text="Litres", font=("arial", 12, "bold"), padx=2, pady=6)
        label_quantity.place(x=170, y=425, width=70, height=25)

        # ***********Check availability Button***********
        button_check_availability = Button(labelFrameLeft, command=self.check_availability, text="Check Availability",
                                           font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        button_check_availability.place(x=3, y=472, width=200, height=32)

        # *******availability status
        entry_availability_status = Entry(labelFrameLeft, textvariable=self.var_check_availability, width=28,
                                          font=("arial", 15, "bold"), state="readonly")
        entry_availability_status.place(x=210, y=472, width=200, height=32)

        # ***********Generate Bill Button***********
        button_generate_bill = Button(labelFrameLeft, command=self.generate_bill, text="Generate Bill",
                                      font=("arial", 14, "bold"), bg="black",
                                      fg="gold", width=9)
        button_generate_bill.place(x=3, y=520, width=200, height=44)

        # ***********Reset Button***********
        button_reset = Button(labelFrameLeft, command=self.reset, text="Reset", font=("arial", 14, "bold"), bg="black",
                              fg="gold", width=9)
        button_reset.place(x=210, y=520, width=200, height=44)

        # *********Billing**********
        labelFrameRight = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details & Search System", padx=2,
                                     font=("times new roman", 12, "bold"))
        labelFrameRight.place(x=435, y=0, width=854, height=610)

        # Bill Number
        label_bill_number = Label(labelFrameRight, text="Bill Number:", fg="gold", font=("arial", 14, "bold"), padx=2,
                                  pady=6, bg="black")
        label_bill_number.place(x=60, y=80, width=200, height=40)
        entry_bill_number = Entry(labelFrameRight, textvariable=self.var_search_bill_number, width=28,
                                  font=("arial", 13))
        entry_bill_number.place(x=290, y=80, width=200, height=40)

        # ***********Reset Button***********
        button_bill_search = Button(labelFrameRight, command=self.search_bill, text="Search",
                                    font=("arial", 14, "bold"), bg="black", fg="gold",
                                    width=9)
        button_bill_search.place(x=530, y=80, width=200, height=39)

        # ***********Bill Label Poster*************

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=600, y=180, width=520, height=380)
        bill = Label(labelFrameRight, text="BILL", font="arial 15 bold", bd=7, relief=GROOVE)
        bill.place(x=0, y=0, width=854, height=40)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        self.welcome_bill("", "", "")

    def welcome_bill(self,billNo, cname, contact):
        if cname != "" or contact != "" or billNo!="":
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\t\t\tWELCOME!\n")
            self.txtarea.insert(END, f"\n BILL NUMBER : {billNo}")
            self.txtarea.insert(END, f"\n CUSTOMER NAME : {cname}")
            self.txtarea.insert(END, f"\n PHONE NUMBER : {contact}")
            self.txtarea.insert(END, f"\n===========================================================")
            self.txtarea.insert(END, f"\n FUEL\t\tQUANTITY\t\tPRICE/L\t\tTOTAL PRICE")
            self.txtarea.insert(END, f"\n===========================================================")
        else:
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\t\t\tWELCOME!\n")
            self.txtarea.insert(END, f"\n BILL NUMBER : {self.var_bill_no.get()}")
            self.txtarea.insert(END, f"\n CUSTOMER NAME : {self.var_customer_name.get()}")
            self.txtarea.insert(END, f"\n PHONE NUMBER : {self.var_contact_number.get()}")
            self.txtarea.insert(END, f"\n===========================================================")
            self.txtarea.insert(END, f"\n FUEL\t\tQUANTITY\t\tPRICE/L\t\tTOTAL PRICE")
            self.txtarea.insert(END, f"\n===========================================================")

    def generate_bill(self):
        if self.var_check_availability.get() == "Available":
            if self.var_contact_number.get() == "" or self.var_customer_name.get() == "" or self.var_quantity.get() == "" or self.var_fuel_type.get() == "":
                messagebox.showerror(title="Error", message="Customer Details are Required",parent=self.root)
            else:
                self.welcome_bill("","","")
                conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                               database="fuel management system")
                my_cursor = conn.cursor()
                query = ("select cost from fuel where fuel=%s")
                value = (self.var_fuel_type.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                total_price = int(row[0]) * int(self.var_quantity.get())
                self.txtarea.insert(END,
                                    f"\n {self.var_fuel_type.get()}\t\t{self.var_quantity.get()}\t\t{str(row[0])}\t\t{total_price}")

                query = ("insert into billDetails values(%s,%s,%s,%s,%s,%s)")
                value = (self.var_bill_no.get(), self.var_customer_name.get(), self.var_contact_number.get(),
                         self.var_fuel_type.get(), self.var_quantity.get(), total_price)
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                self.save_bill()

        else:
            messagebox.showerror(title="Error", message="Not Available",parent=self.root)

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("D:\\pythonProjects\\Fuel Management System\\billPage/" + str(self.var_bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill No :{self.var_bill_no.get()} Saved Successfully")
        else:
            return

    def search_bill(self):
        if self.var_search_bill_number.get() == "":
            messagebox.showerror(title="Error", message="Bill number required for bill searching",parent=self.root)
        else:
            self.welcome_bill("", "", "")
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                           database="fuel management system")
            my_cursor = conn.cursor()
            query = ("select * from billDetails where billNo=%s")
            value = (self.var_search_bill_number.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            self.welcome_bill(row[0],row[1], row[2])
            # print(row)
            ppl = int(row[5]) / int(row[4])
            self.txtarea.insert(END, f"\n {row[3]}\t\t{row[4]}\t\t{str(ppl)}\t\t{row[5]}")

            conn.commit()
            conn.close()

    def fetch_data(self):
        if self.var_contact_number.get() == "":
            messagebox.showerror(title="Error", message="Enter contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                           database="fuel management system")
            my_cursor = conn.cursor()
            query = (
                "select cname,licensenumber,modelnumber,carnumber,gender,email,state,city,postcode from customer where mobile=%s")
            value = (self.var_contact_number.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror(title="Error", message="Contact Number not Registered",parent=self.root)
            else:
                self.var_customer_name.set(row[0])
                self.var_license_number.set(row[1])
                self.var_model_number.set(row[2])
                self.var_car_number.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_state.set(row[6])
                self.var_city.set(row[7])
                self.var_post_code.set(row[8])
            conn.commit()
            conn.close()

    def check_availability(self):
        if self.var_quantity.get() == "":
            messagebox.showerror(title="Error", message="Enter quantity",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                           database="fuel management system")
            my_cursor = conn.cursor()
            query = ("select capacity from fuel where fuel=%s")
            value = (self.var_fuel_type.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(int(row[0]))
            if int(self.var_quantity.get()) <= int(row[0]):
                self.var_check_availability.set("Available")
                value = str(int(row[0]) - int(self.var_quantity.get()))
                print(value)
                print(str(value))
                query = ("Update fuel set capacity=%s where fuel=%s")
                value = (value, self.var_fuel_type.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
            else:
                self.var_check_availability.set("Not Available")
            conn.commit()
            conn.close()

    def reset(self):

        self.var_contact_number.set("")
        self.var_customer_name.set("")
        self.var_license_number.set("")
        self.var_model_number.set("")
        self.var_car_number.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_post_code.set("")
        self.var_quantity.set("")
        self.var_check_availability.set("")


if __name__ == '__main__':
    root = Tk()
    obj = Buying(root)
    root.mainloop()
