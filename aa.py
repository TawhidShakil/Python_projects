import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("1350x700+0+0")
window.title("Student Management System")
#create a label for heading
lbl_heading = tk.Label(
    master= window, 
    text="Student Mangement System",
    font=("Helvetica", 30, "bold"),
    border=10, relief=tk.GROOVE,
    bg= "lightgrey"
)
lbl_heading.pack(side=tk.TOP, fill=tk.X)

# create a details frame
frm_detail = tk.LabelFrame(
    master= window,
    text = "Enter Details",
    font = ("Helvetica", 20), 
    border=10, relief=tk.GROOVE, 
    bg="lightgrey"

)

frm_detail.place(x = 20, y =90, width=420, height=575)
frm_data = tk.Frame(
    master=window,
    bd = 12, bg = "lightgrey", relief=tk.GROOVE
)

frm_data.place(x = 475, y = 90, width=810, height=575)

# ========= Entry =======

#label for roll num
lbl_rollNo = tk.Label(
    master= frm_detail,
    text="ID No",
    font=("Helvetica", 18), 
    bg="lightgrey"
)
lbl_rollNo.grid(row=0, column=0, padx=2, pady=2)

# create a entry box for roll no
ent_rollNo = tk.Entry(
    master=frm_detail,
    bd= 5,
    width=20,
    font=("Helvetica", 12)
)

ent_rollNo.grid(row= 0, column=1, padx=2, pady=2)


#label for Full name
lbl_fullName = tk.Label(master=frm_detail, text="Name", font=("Helvetica", 18), bg="lightgrey")
lbl_fullName.grid(row=1, column=0, padx=2 , pady=2)

ent_fullName = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12))
ent_fullName.grid(row=1, column=1, padx=2, pady=2)

# label for e-mail
lbl_email = tk.Label(master=frm_detail, text="E-mail", font=("Helvetica", 18), bg="lightgrey")
lbl_email.grid(row=2, column=0, padx=2 , pady=2)

ent_email = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12))
ent_email.grid(row=2, column=1, padx=2, pady=2)

# label for gender
lbl_gender = tk.Label(master=frm_detail, text="Gender", font=("Helvetica", 18), bg="lightgrey")
lbl_gender.grid(row=3, column=0, padx=2 , pady=2)

ent_gender = ttk.Combobox(master=frm_detail, font=("Helvetica", 12), state="readonly")
ent_gender['values'] = ("Male", "Female", "Others")
ent_gender.grid(row=3, column=1, padx=2, pady=2)

#label for date of birth
lbl_dateOfBirth = tk.Label(master=frm_detail, text="D.O.B", font=("Helvetica", 18), bg="lightgrey")
lbl_dateOfBirth.grid(row=4, column=0, padx=2 , pady=2)

ent_dateOfBirth = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12) )
ent_dateOfBirth.grid(row=4, column=1, padx=2, pady=2)

# label for phone number
lbl_phone = tk.Label(master=frm_detail, text="Phone", font=("Helvetica", 18), bg="lightgrey")
lbl_phone.grid(row=5, column=0, padx=2 , pady=2)

ent_phone = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12) )
ent_phone.grid(row=5, column=1, padx=2, pady=2)

#label for department 
lbl_department = tk.Label(master=frm_detail, text="Department", font=("Helvetica", 18), bg="lightgrey")
lbl_department.grid(row=6, column=0, padx=2 , pady=2)

ent_department = tk.Entry(master=frm_detail, width=20, bd=5, font=("Helvetica", 12))
ent_department.grid(row=6, column=1, padx=2, pady=2)



#============ ============#

# ============= start the button frame ================#

btn_frame = tk.Frame(master=frm_detail, bd= 5, bg="lightgrey", relief=tk.GROOVE)
btn_frame.place(x = 30, y= 350, width=350, height=100)

# button for add student
btn_add = tk.Button(master=btn_frame, text="ADD", font=("Helvetica", 10), bg="green", fg="white", bd=7,width=5)
btn_add.place(x=10, y=30)

# button for UPDATE
btn_update = tk.Button(master=btn_frame, text="UPDATE", font=("Helvetica", 10), bg="orange", fg="black", bd=7)
btn_update.place(x=80, y=30)

#button for DELETE 
btn_delete = tk.Button(master=btn_frame, text="DELETE", font=("Helvetica", 10), bg="red", fg="white", bd=7)
btn_delete.place(x=170, y=30)

# button for CLEAR
btn_clear = tk.Button(master=btn_frame, text="CLEAR", font=("Helvetica", 10), bg="blue", fg="white", bd=7)
btn_clear.place(x=260, y=30)

# ============= End the button frame ==================#

# ============== Create a SEARCH Frame ========#

search_frm = tk.Frame(master= frm_data, bg="lightgrey", bd=10, relief= tk.GROOVE)
search_frm.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(master=search_frm, text="Search By ID", font=("Helvetica", 14))
search_lbl.grid(row=0, column=0, padx=12, pady=2)

search_comboBox = ttk.Combobox(master=search_frm, font=("Helvetica", 14), state="readonly")
search_comboBox ['values'] = ("ID NO", "E-MAIL")
search_comboBox.grid(row=0, column=1, padx=12, pady=2)

search_btn = tk.Button(master=search_frm, text="Search", font=("Helvetica", 12), bg="blue", fg="White", width=10, bd=5)
search_btn.grid(row=0, column=2, padx=12, pady=2)

showAll_btn = tk.Button(master=search_frm, text="Show All", font=("Helvetica", 12), bg="green", fg="White",  width=10, bd=5)
showAll_btn.grid(row=0, column=3, padx=12, pady=2)


# ============== END Search Frame =============#

# =============== DATABASE frame ===============#
main_frm = tk. Frame(master=frm_data, bg ="lightgrey", bd=11, relief=tk.GROOVE)
main_frm.pack(fill= tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frm, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frm, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(master=main_frm, columns=("ID No.", "Name", "E-mail", "Phone", "Gender", "D.O.B", "Department"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)
y_scroll.pack(side=tk.RIGHT, fill= tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill= tk.X)

student_table.heading("ID No.", text="ID No.")
student_table.heading("Name", text="Name")
student_table.heading("E-mail", text="E-mail")
student_table.heading("Phone", text="Phone")
student_table.heading("Gender", text="Gender")
student_table.heading("D.O.B", text="D.O.B")
student_table.heading("Department", text="Department")

student_table['show'] = 'headings'

student_table.column("ID No.", width=100)
student_table.column("Name", width=100)
student_table.column("E-mail", width=100)
student_table.column("Phone", width=100)
student_table.column("Gender", width=100)
student_table.column("D.O.B", width=100)
student_table.column("Department", width=100)

student_table.pack(fill=tk.BOTH, expand=True)

# =============== END DATABASE frame ===========#

window.mainloop()