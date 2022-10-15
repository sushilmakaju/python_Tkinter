import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Gui practice")
window.geometry("250x150")
window.resizable(0, False)

##label
user = ttk.Label(window, text="name : ", foreground="Black")
user.grid(row=2, column=0)

password = ttk.Label(window, text="age : ", foreground="Black")
password.grid(row=3, column=0)

District = ttk.Label(window, text="District : ", foreground="Black")
District.grid(row=4, column=0)

genderlbl = ttk.Label(window, text="Gender : ", foreground="Black")
genderlbl.grid(row=5, column=0)

##text feild
user_var = tk.StringVar()  # to store value
user_entry = ttk.Entry(window,  textvariable=user_var)
user_entry.grid(row=2, column=2)

pass_var = tk.StringVar()
pass_entry = ttk.Entry(window, textvariable=pass_var)
pass_entry.grid(row=3, column=2)

# combobox
District_var = tk.StringVar()
District_combo = ttk.Combobox(window, width=16, textvariable=District_var, state='readonly')
# Adding values in cmbbox
District_combo['values'] = ('Bhaktapur', 'Lalitpur', 'Kathmandu')

# to keep current value in cmbbox
District_combo.current(0)

# setting positon in gridlayout
District_combo.grid(row=4, column=2, columnspan=3)

# Radiobutton\
gender_radio = tk.StringVar()
gender_radio1 = ttk.Radiobutton(window, text="male", value="Male", variable=gender_radio)
gender_radio1.grid(row=5, column=1, columnspan=1)

gender_radio2 = ttk.Radiobutton(window, text="female", value="Female", variable=gender_radio)
gender_radio2.grid(row=5, column=2,columnspan=4)

#checkbutton
check_btn_var = tk.IntVar()
check_btn = ttk.Checkbutton(window, text='Do you like coffee', variable=check_btn_var)
check_btn.grid(row=6, columnspan=3)


# button
def login():
    userobj = user_var.get()
    passobj = pass_var.get()
    dis_obj = District_var.get()
    radio_obj = gender_radio.get()
    if check_btn_var.get() == 0:
        coffee = "No he doesn't likes coffee"
    else:
         coffee = "yes he likes coffee"
    print(f'{userobj} is  {passobj} years old who lives in {dis_obj} district. His gender is {radio_obj}  {coffee}')


sumbit_btn = ttk.Button(window, text="sumbit", command=login)
sumbit_btn.grid(row=60, column=2)

close_btn = ttk.Button(window, text="Close", command=window.destroy)
close_btn.grid(row=90, column=2)

window.mainloop()
