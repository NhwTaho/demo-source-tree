import tkinter as tk
from tkinter import ttk

class DataEntryFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")
        self.root.geometry("500x400")

        # User Information Frame
        self.user_info_frame = tk.LabelFrame(root, text="User Information")
        self.user_info_frame.pack(fill="both", expand="yes", padx=20, pady=10)

        tk.Label(self.user_info_frame, text="First Name").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.user_info_frame, text="Last Name").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.user_info_frame, text="Title").grid(row=0, column=2, padx=10, pady=5)

        self.first_name_entry = tk.Entry(self.user_info_frame)
        self.last_name_entry = tk.Entry(self.user_info_frame)
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=["Mr.", "Mrs.", "Miss", "Dr.", "Prof."])

        self.first_name_entry.grid(row=1, column=0, padx=10, pady=5)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.title_combobox.grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self.user_info_frame, text="Age").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.user_info_frame, text="Nationality").grid(row=2, column=1, padx=10, pady=5)

        self.age_spinbox = tk.Spinbox(self.user_info_frame, from_=1, to=100)
        self.nationality_entry = tk.Entry(self.user_info_frame)

        self.age_spinbox.grid(row=3, column=0, padx=10, pady=5)
        self.nationality_entry.grid(row=3, column=1, padx=10, pady=5)

        # Registration Status Frame
        self.registration_frame = tk.LabelFrame(root, text="Registration Status")
        self.registration_frame.pack(fill="both", expand="yes", padx=20, pady=10)

        self.currently_registered_var = tk.BooleanVar()
        self.currently_registered_checkbox = tk.Checkbutton(self.registration_frame, text="Currently Registered", variable=self.currently_registered_var)
        self.currently_registered_checkbox.grid(row=0, column=0, padx=10, pady=5)

        tk.Label(self.registration_frame, text="# Completed Courses").grid(row=0, column=1, padx=10, pady=5)
        self.completed_courses_spinbox = tk.Spinbox(self.registration_frame, from_=0, to=50)
        self.completed_courses_spinbox.grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self.registration_frame, text="# Semesters").grid(row=1, column=1, padx=10, pady=5)
        self.semesters_spinbox = tk.Spinbox(self.registration_frame, from_=0, to=10)
        self.semesters_spinbox.grid(row=1, column=2, padx=10, pady=5)

        # Terms & Conditions Frame
        self.terms_frame = tk.LabelFrame(root, text="Terms & Conditions")
        self.terms_frame.pack(fill="both", expand="yes", padx=20, pady=10)

        self.terms_var = tk.BooleanVar()
        self.terms_checkbox = tk.Checkbutton(self.terms_frame, text="I accept the terms and conditions.", variable=self.terms_var)
        self.terms_checkbox.pack(padx=10, pady=5)

        # Submit Button
        self.submit_button = tk.Button(root, text="Enter data", command=self.submit_data)
        self.submit_button.pack(pady=20)

    def submit_data(self):
        print("First Name:", self.first_name_entry.get())
        print("Last Name:", self.last_name_entry.get())
        print("Title:", self.title_combobox.get())
        print("Age:", self.age_spinbox.get())
        print("Nationality:", self.nationality_entry.get())
        print("Currently Registered:", self.currently_registered_var.get())
        print("# Completed Courses:", self.completed_courses_spinbox.get())
        print("# Semesters:", self.semesters_spinbox.get())
        print("Accepted Terms:", self.terms_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryFormApp(root)
    root.mainloop()