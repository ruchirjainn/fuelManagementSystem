# ***************CODE BY RUCHIR JAIN**********************
from tkinter import *


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuel Management System")
        self.root.geometry("1295x700+230+170")

        # ********Upper Frame***************
        upper_frame = LabelFrame(self.root, bd=2, bg="black", fg="gold", relief=RIDGE, text="About", padx=2,
                                 font=("times new roman", 12, "bold"))
        upper_frame.place(x=0, y=0, width=1295, height=130)

        desc = """
I, Ruchir Jain, am an enthusiastic and dedicated engineering student currently studying at Swami Vivekananda College of Engineering. I am passionate about learning, particularly in the areas of computer science and software development. With a strong drive for personal growth and a commitment to academic excellence, I am confident in my ability to contribute to the field of engineering and achieve my career aspirations.                """
        label_intro = Label(upper_frame, text=desc, fg="gold", bg="black", font=("Arial", 12), justify=CENTER,
                            wraplength=1100)
        label_intro.pack(padx=20)

        # ********Lower Frame***************
        lower_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Project Report", bg="black", fg="gold", padx=2,
                                 font=("times new roman", 12, "bold"))
        lower_frame.place(x=0, y=130, width=1295, height=480)

        label = Label(lower_frame, text="Report Description", bg="black", fg="gold", font=("Arial", 24, "bold"))
        label.place(x=500, y=18)

        description = """
        This Fuel Management System allows users to efficiently manage and track fuel usage and inventory.

        Features of the system include:

        - This system works with user's and admin
        - Adding fuel entries with details such as date, fuel type and cost.
        - Viewing and searching fuel inventory.
        - Saving reports based on fuel cost updates and inventory.
        - Tabular representation of data.
        - User authentication and access control to ensure data security.
        - Integration with external systems such as fuel suppliers or accounting software.
        - Historical data tracking of fuel and analysis for better decision making.

        The Fuel Management System provides a user-friendly interface and a seamless experience for managing fuel-related operations in various industries such as transportation, logistics, and construction.

        For any assistance or issues, please contact the administrator.
        
        Regards,
        Ruchir Jain
        """

        label_info = Label(lower_frame, text=description, bg="black", fg="gold", font=("Arial", 12), justify=LEFT,
                           wraplength=1100)
        label_info.place(x=160, y=57)


if __name__ == '__main__':
    root = Tk()
    root.configure(bg="white")
    root.attributes('-alpha', 0.95)
    obj = Report(root)
    root.mainloop()
