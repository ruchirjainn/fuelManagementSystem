# ***************CODE BY RUCHIR JAIN**********************
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class RegisterCustomer:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Management System")
        self.root.geometry("1295x700+230+170")

        # *********Variables*********
        self.var_cust_name = StringVar()
        self.var_mother_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_post_code = StringVar()
        self.var_mobile_number = StringVar()
        self.var_email = StringVar()
        self.var_type_car = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_model_number = StringVar()
        self.var_car_number = StringVar()
        self.var_license_number = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()

        # ******Label Frame***********
        labelFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelFrameLeft.place(x=0, y=0, width=425, height=610)

        # **********Labels & entries*********

        # customer name
        label_cust_name = Label(labelFrameLeft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_cust_name.grid(row=0, column=0, sticky=W)
        entry_cust_name = ttk.Entry(labelFrameLeft, textvariable=self.var_cust_name, width=28, font=("arial", 13))
        entry_cust_name.grid(row=0, column=1)

        # mother name
        label_mother_name = Label(labelFrameLeft, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_mother_name.grid(row=2, column=0, sticky=W)
        entry_mother_name = ttk.Entry(labelFrameLeft, textvariable=self.var_mother_name, width=28, font=("arial", 13))
        entry_mother_name.grid(row=2, column=1)

        # age
        label_age = Label(labelFrameLeft, text="Age:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_age.grid(row=4, column=0, sticky=W)
        entry_age = ttk.Entry(labelFrameLeft, textvariable=self.var_age, width=28, font=("arial", 13))
        entry_age.grid(row=4, column=1)

        # gender combobox
        label_gender = Label(labelFrameLeft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=6, column=0, sticky=W)
        gender_combo = ttk.Combobox(labelFrameLeft, textvariable=self.var_gender, font=("arial", 12), width=26,
                                    state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=6, column=1)

        # postcode
        label_post_code = Label(labelFrameLeft, text="Post Code:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_post_code.grid(row=8, column=0, sticky=W)
        entry_post_code = ttk.Entry(labelFrameLeft, textvariable=self.var_post_code, width=28, font=("arial", 13))
        entry_post_code.grid(row=8, column=1)

        # mobile number
        label_mobile_number = Label(labelFrameLeft, text="Mobile Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_mobile_number.grid(row=10, column=0, sticky=W)
        entry_mobile_number = ttk.Entry(labelFrameLeft, textvariable=self.var_mobile_number, width=28,
                                        font=("arial", 13))
        entry_mobile_number.grid(row=10, column=1)

        # email
        label_email = Label(labelFrameLeft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_email.grid(row=12, column=0, sticky=W)
        entry_email = ttk.Entry(labelFrameLeft, textvariable=self.var_email, width=28, font=("arial", 13))
        entry_email.grid(row=12, column=1)

        # type of car
        label_type_car = Label(labelFrameLeft, text="Type Of Car:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_type_car.grid(row=14, column=0, sticky=W)
        type_car_combo = ttk.Combobox(labelFrameLeft, textvariable=self.var_type_car, font=("arial", 12), width=26,
                                      state="readonly")
        type_car_combo["values"] = ("Two Wheeler", "Three Wheeler", "Four Wheeler")
        type_car_combo.current(0)
        type_car_combo.grid(row=14, column=1)

        # idproof type combobox
        label_id_proof = Label(labelFrameLeft, text="Id Proof Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_id_proof.grid(row=16, column=0, sticky=W)
        id_proof_combo = ttk.Combobox(labelFrameLeft, textvariable=self.var_id_proof, font=("arial", 12), width=26,
                                      state="readonly")
        id_proof_combo["values"] = ("Aadhar Card", "Pan Card", "Passport")
        id_proof_combo.current(0)
        id_proof_combo.grid(row=16, column=1)

        # id number
        label_id_number = Label(labelFrameLeft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_id_number.grid(row=18, column=0, sticky=W)
        entry_id_number = ttk.Entry(labelFrameLeft, textvariable=self.var_id_number, width=28, font=("arial", 13))
        entry_id_number.grid(row=18, column=1)

        # model number
        label_mode_no = Label(labelFrameLeft, text="Model Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_mode_no.grid(row=20, column=0, sticky=W)
        entry_mode_no = ttk.Entry(labelFrameLeft, textvariable=self.var_model_number, width=28, font=("arial", 13))
        entry_mode_no.grid(row=20, column=1)

        # car number
        label_car_no = Label(labelFrameLeft, text="Car Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_car_no.grid(row=22, column=0, sticky=W)
        entry_car_no = ttk.Entry(labelFrameLeft, textvariable=self.var_car_number, width=28, font=("arial", 13))
        entry_car_no.grid(row=22, column=1)

        # license number
        label_license_no = Label(labelFrameLeft, text="License Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_license_no.grid(row=24, column=0, sticky=W)
        entry_license_no = ttk.Entry(labelFrameLeft, textvariable=self.var_license_number, width=28, font=("arial", 13))
        entry_license_no.grid(row=24, column=1)

        # city
        label_state = Label(labelFrameLeft, text="State:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_state.grid(row=26, column=0, sticky=W)
        entry_state = ttk.Entry(labelFrameLeft, textvariable=self.var_state, width=28, font=("arial", 13))
        entry_state.grid(row=26, column=1)

        # city
        label_city = Label(labelFrameLeft, text="City:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_city.grid(row=28, column=0, sticky=W)
        entry_city = ttk.Entry(labelFrameLeft, textvariable=self.var_city, width=28, font=("arial", 13))
        entry_city.grid(row=28, column=1)

        # ********Buttons*****************
        button_frame = Frame(labelFrameLeft, bd=2, relief=RIDGE)
        button_frame.place(x=0, y=530, width=412, height=40)

        button_add = Button(button_frame, command=self.add_data, text="Add", font=("arial", 12, "bold"), bg="black",
                            fg="gold", width=9)
        button_add.grid(row=0, column=0, padx=1)

        button_update = Button(button_frame, command=self.update, text="Update", font=("arial", 12, "bold"), bg="black",
                               fg="gold", width=9)
        button_update.grid(row=0, column=1, padx=1)

        button_delete = Button(button_frame, command=self.delete_customer, text="Delete", font=("arial", 12, "bold"),
                               bg="black", fg="gold", width=9)
        button_delete.grid(row=0, column=2, padx=1)

        button_reset = Button(button_frame, command=self.reset, text="Reset", font=("arial", 12, "bold"), bg="black",
                              fg="gold", width=9)
        button_reset.grid(row=0, column=3, padx=1)

        # *********Table Frame Search system**********
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details & Search System", padx=2,
                                 font=("times new roman", 12, "bold"))
        table_Frame.place(x=435, y=0, width=854, height=610)

        label_search_by = Label(table_Frame, text="Search By:", font=("arial", 12, "bold"), bg="green", fg="white")
        label_search_by.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        SearchBy_combo = ttk.Combobox(table_Frame, textvariable=self.search_var, font=("arial", 12), width=24,
                                      state="readonly")
        SearchBy_combo["values"] = ("mobile", "licensenumber")
        SearchBy_combo.current(0)
        SearchBy_combo.grid(row=0, column=1, padx=2)

        self.var_search_by = StringVar()
        entry_search_by = ttk.Entry(table_Frame, textvariable=self.var_search_by, width=24, font=("arial", 13))
        entry_search_by.grid(row=0, column=2, padx=2)

        button_search = Button(table_Frame, command=self.search, text="Search", font=("arial", 12, "bold"), bg="black",
                               fg="gold", width=9)
        button_search.grid(row=0, column=3, padx=1)

        button_show_all = Button(table_Frame, command=self.fetch_data, text="Show All", font=("arial", 12, "bold"),
                                 bg="black", fg="gold", width=9)
        button_show_all.grid(row=0, column=4, padx=1)

        # ************Show Data Table & Scroll Bar*******
        details_table_frame = Frame(table_Frame, bd=2, relief=RIDGE)
        details_table_frame.place(x=0, y=40, width=855, height=535)

        scroll_x = ttk.Scrollbar(details_table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table_frame, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table_frame,
                                               columns=("cname", "mname", "age", "gender", "postcode", "mobile",
                                                        "email", "typecar", "idproof", "idnumber", "modelnumber",
                                                        "carnumber", "licensenumber", "state", "city"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("cname", text="Customer Name")
        self.Cust_Details_Table.heading("mname", text="Mother Name")
        self.Cust_Details_Table.heading("age", text="Age")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("postcode", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("typecar", text="Type Of Car")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("modelnumber", text="Model Number")
        self.Cust_Details_Table.heading("carnumber", text="Car Number")
        self.Cust_Details_Table.heading("licensenumber", text="License Number")
        self.Cust_Details_Table.heading("state", text="State")
        self.Cust_Details_Table.heading("city", text="City")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("cname", width=100)
        self.Cust_Details_Table.column("mname", width=100)
        self.Cust_Details_Table.column("age", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("postcode", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("typecar", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("modelnumber", width=100)
        self.Cust_Details_Table.column("carnumber", width=100)
        self.Cust_Details_Table.column("licensenumber", width=100)
        self.Cust_Details_Table.column("state", width=100)
        self.Cust_Details_Table.column("city", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):  # from entry values to tables
        if self.var_mobile_number.get() == "" or self.var_license_number.get() == "" or self.var_mother_name.get() == "":
            messagebox.showerror(title="Error", message="All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                               database="fuel management system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_cust_name.get(),
                    self.var_mother_name.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_post_code.get(),
                    self.var_mobile_number.get(),
                    self.var_email.get(),
                    self.var_type_car.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_model_number.get(),
                    self.var_car_number.get(),
                    self.var_license_number.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(title="Success", message="Customer Details has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning(title="Warning", message=f"Some thing went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):  # tables m values aateh from database
        conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                       database="fuel management system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        else:
            messagebox.showwarning(title="Warning", message="No Details Found 404!, Please add details",parent=self.root)
        conn.close()

    def get_cursor(self, event=""):  # table se row click karne k baad automatic values aajate h
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        # print(content)
        row = content["values"]

        self.var_cust_name.set(row[0])
        self.var_mother_name.set(row[1])
        self.var_age.set(row[2])
        self.var_gender.set(row[3])
        self.var_post_code.set(row[4])
        self.var_mobile_number.set(row[5])
        self.var_email.set(row[6])
        self.var_type_car.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_model_number.set(row[10])
        self.var_car_number.set(row[11])
        self.var_license_number.set(row[12])
        self.var_state.set(row[13])
        self.var_city.set(row[14])

    def update(self):
        if self.var_mobile_number.get() == "":
            messagebox.showerror(title="Error", message="Enter Mobile Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                           database="fuel management system")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update customer set cname=%s,mname=%s,age=%s,gender=%s,postcode=%s,email=%s,typecar=%s,idproof=%s,idnumber=%s,modelnumber=%s,carnumber=%s,licensenumber=%s,state=%s,city=%s where mobile=%s",
                (
                    self.var_cust_name.get(),
                    self.var_mother_name.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_post_code.get(),
                    self.var_email.get(),
                    self.var_type_car.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_model_number.get(),
                    self.var_car_number.get(),
                    self.var_license_number.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_mobile_number.get(),
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(title="Success", message="Customer Details Updated Successfully", parent=self.root)

    def delete_customer(self):
        mDelete = messagebox.askyesno(title="Fuel Management System", message="Do you want to delete this customer?",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                           database="fuel management System")
            my_cursor = conn.cursor()
            query = "delete from customer where mobile=%s"
            values = (self.var_mobile_number.get(),)
            my_cursor.execute(query, values)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_cust_name.set("")
        self.var_mother_name.set("")
        self.var_age.set("")
        # self.var_gender.set("")
        self.var_post_code.set("")
        self.var_mobile_number.set("")
        self.var_email.set("")
        # self.var_type_car.set("")
        # self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_model_number.set("")
        self.var_car_number.set("")
        self.var_license_number.set("")
        self.var_state.set("")
        self.var_city.set("")

    def search(self):
        if self.var_search_by.get()=="":
            messagebox.showerror(title="Error",message="Details Not found",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",database="fuel management system")
            my_cursor = conn.cursor()
            # if self.search_var.get()=="mobile":
            #     my_cursor.execute("select * from customer where mobile="+str(self.txt_search.get()))
            my_cursor.execute(
                "select * from customer where " + str(self.search_var.get()) + "=" + str(self.var_search_by.get()))
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showerror(title="Not Found", message="Data Not Found",parent=self.root)
            conn.close()


if __name__ == '__main__':
    root = Tk()
    obj = RegisterCustomer(root)
    root.mainloop()
