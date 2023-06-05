# ***************CODE BY RUCHIR JAIN**********************
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk


class Inventory:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Management System")
        self.root.geometry("1295x700+230+170")

        # *********Variables*********
        self.var_fuel_type = StringVar()
        self.var_fuel_current_price = StringVar()
        self.var_fuel_current_capacity = StringVar()

        self.var_fuel = StringVar()
        self.var_fuel_updated_price = StringVar()
        self.var_date = StringVar()
        self.var_fuel_updated_capacity = StringVar()

        # ******Label Frame***********
        labelFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Fuel Inventory", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelFrameLeft.place(x=0, y=0, width=425, height=610)

        # **********Labels & entries*********

        # type of fuel
        label_type_of_fuel = Label(labelFrameLeft, text="Type Of Fuel:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_type_of_fuel.grid(row=0, column=0, sticky=W)
        combo_fuel_type = ttk.Combobox(labelFrameLeft, textvariable=self.var_fuel_type, font=("arial", 12), width=26,
                                       state="readonly")
        combo_fuel_type["values"] = ("PETROL", "CNG", "DIESEL")
        combo_fuel_type.current(0)
        combo_fuel_type.grid(row=0, column=1)

        # Current Price
        label_current_cost_of_fuel = Label(labelFrameLeft, text="Current Price:", font=("arial", 12, "bold"), padx=2,
                                           pady=6)
        label_current_cost_of_fuel.grid(row=1, column=0, sticky=W)
        entry_current_cost_of_fuel = ttk.Entry(labelFrameLeft, textvariable=self.var_fuel_current_price, width=28,
                                               font=("arial", 13), state="readonly")
        entry_current_cost_of_fuel.grid(row=1, column=1)

        # Current Capacity
        label_current_cost_of_fuel = Label(labelFrameLeft, text="Current Capacity:", font=("arial", 12, "bold"), padx=2,
                                           pady=6)
        label_current_cost_of_fuel.grid(row=2, column=0, sticky=W)
        entry_current_cost_of_fuel = ttk.Entry(labelFrameLeft, textvariable=self.var_fuel_current_capacity, width=28,
                                               font=("arial", 13), state="readonly")
        entry_current_cost_of_fuel.grid(row=2, column=1)

        # Fetch current price button
        button_fetch_current_price = Button(labelFrameLeft, command=self.fetch_current_price_capacity,
                                            text="Fetch Current Price", font=("arial", 12, "bold"),
                                            bg="black", fg="gold", width=9)
        button_fetch_current_price.place(x=115, y=114, width=200)

        # ******Label Frame in left label frame***********
        labelFrameInsideFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Update Current Fuel Data", padx=2,
                                           font=("times new roman", 12, "bold"))
        labelFrameInsideFrame.place(x=10, y=180, width=400, height=430)

        # **********Labels & entries in inside label frame*********

        # Type Of fuel
        label_type_of_fuel = Label(labelFrameInsideFrame, text="Type Of Fuel:", font=("arial", 12, "bold"), padx=2,
                                   pady=6)
        label_type_of_fuel.grid(row=0, column=0, sticky=W)
        combo_fuel_type = ttk.Combobox(labelFrameInsideFrame, textvariable=self.var_fuel, font=("arial", 12), width=21,
                                       state="readonly")
        combo_fuel_type["values"] = ("PETROL", "CNG", "DIESEL")
        combo_fuel_type.current(0)
        combo_fuel_type.grid(row=0, column=1)

        # Updated Price
        label_updated_price_of_fuel = Label(labelFrameInsideFrame, text="Updated Price:", font=("arial", 12, "bold"),
                                            padx=2, pady=6)
        label_updated_price_of_fuel.grid(row=1, column=0, sticky=W)
        entry_updated_price_of_fuel = ttk.Entry(labelFrameInsideFrame, textvariable=self.var_fuel_updated_price,
                                                width=23, font=("arial", 13))
        entry_updated_price_of_fuel.grid(row=1, column=1)

        # Date
        label_date = Label(labelFrameInsideFrame, text="Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_date.grid(row=2, column=0, sticky=W)
        entry_date = ttk.Entry(labelFrameInsideFrame, textvariable=self.var_date, width=23, font=("arial", 13))
        entry_date.grid(row=2, column=1)

        # Capacity
        label_date = Label(labelFrameInsideFrame, text="Updated Capacity:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_date.grid(row=3, column=0, sticky=W)
        entry_date = ttk.Entry(labelFrameInsideFrame, textvariable=self.var_fuel_updated_capacity, width=23,
                               font=("arial", 13))
        entry_date.grid(row=3, column=1)

        # ********Buttons*****************

        button_update = Button(labelFrameInsideFrame, command=self.update_data, text="Update",
                               font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        button_update.place(x=80, y=155)

        button_reset = Button(labelFrameInsideFrame, command=self.reset, text="Reset", font=("arial", 12, "bold"),
                              bg="black", fg="gold", width=9)
        button_reset.place(x=220, y=155)

        # *********Image in label frame inside wala**************
        img1 = Image.open(r"D:\pythonProjects\Fuel Management System\Image\posterInInventory.jpg")
        img1 = img1.resize((390, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(labelFrameInsideFrame, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=200, width=390, height=200)

        # *********Table Frame Search system**********
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Fuel Details & Search System", padx=2,
                                 font=("times new roman", 12, "bold"))
        table_Frame.place(x=435, y=0, width=854, height=610)

        label_search_by = Label(table_Frame, text="Search By:", font=("arial", 12, "bold"), bg="green", fg="white")
        label_search_by.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        SearchBy_combo = ttk.Combobox(table_Frame, textvariable=self.search_var, font=("arial", 12), width=24,
                                      state="readonly")
        SearchBy_combo["values"] = ("dateOfNewStock", "fuelType")
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

        self.Fuel_Details_Table = ttk.Treeview(details_table_frame,
                                               columns=("dateOfNewStock", "fuelType", "costOfFuel", "capacityFuel"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Fuel_Details_Table.xview)
        scroll_y.config(command=self.Fuel_Details_Table.yview)

        self.Fuel_Details_Table.heading("dateOfNewStock", text="Date Of New Stock")
        self.Fuel_Details_Table.heading("fuelType", text="Fuel Type")
        self.Fuel_Details_Table.heading("costOfFuel", text="Fuel Cost")
        self.Fuel_Details_Table.heading("capacityFuel", text="Fuel Capacity")

        self.Fuel_Details_Table["show"] = "headings"

        self.Fuel_Details_Table.column("dateOfNewStock", width=100)
        self.Fuel_Details_Table.column("fuelType", width=100)
        self.Fuel_Details_Table.column("costOfFuel", width=100)
        self.Fuel_Details_Table.column("capacityFuel", width=100)

        self.Fuel_Details_Table.pack(fill=BOTH, expand=1)
        # self.Fuel_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def update_data(self):  # from entry values to tables
        if self.var_fuel.get() == "" or self.var_fuel_updated_price.get() == "":
            messagebox.showerror(title="Error", message="All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                               database="fuel management system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into inventory values(%s,%s,%s,%s)", (
                    self.var_date.get(),
                    self.var_fuel.get(),
                    self.var_fuel_updated_price.get(),
                    self.var_fuel_updated_capacity.get()
                ))
                my_cursor.execute("Update fuel set cost=%s,capacity=%s where fuel=%s", (
                    self.var_fuel_updated_price.get(),
                    self.var_fuel_updated_capacity.get(),
                    self.var_fuel.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(title="Success", message="Fuel Cost updated successfull", parent=self.root)
            except Exception as es:
                messagebox.showwarning(title="Warning", message=f"Some thing went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                       database="fuel management system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from inventory")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Fuel_Details_Table.delete(*self.Fuel_Details_Table.get_children())
            for i in rows:
                self.Fuel_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def fetch_current_price_capacity(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                       database="fuel management system")
        my_cursor = conn.cursor()
        query = ("select cost,capacity from fuel where fuel=%s")
        value = (self.var_fuel_type.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()
        print(row[0])
        self.var_fuel_current_price.set(row[0])
        self.var_fuel_current_capacity.set(row[1])

    def reset(self):
        self.var_fuel_current_price.set("")
        self.var_fuel_updated_price.set("")
        self.var_date.set("")
        self.var_fuel_updated_capacity.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@Ruchir2003",
                                       database="fuel management system")
        my_cursor = conn.cursor()
        if self.search_var.get() == "dateOfNewStock":
            query = ("select * from inventory where dateOfNewStock=%s")
            value = (self.var_search_by.get(),)
            my_cursor.execute(query, value)
        else:
            query = ("select * from inventory where fuelType=%s")
            value = (self.var_search_by.get(),)
            my_cursor.execute(query, value)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Fuel_Details_Table.delete(*self.Fuel_Details_Table.get_children())
            for i in rows:
                self.Fuel_Details_Table.insert("", END, values=i)
            conn.commit()
        else:
            messagebox.showerror(title="Not Found", message="Data Not Found",parent=self.root)
        conn.close()


if __name__ == '__main__':
    root = Tk()
    obj = Inventory(root)
    root.mainloop()
