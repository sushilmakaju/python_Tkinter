import tkinter
from  tkinter import*

window = Tk()
window.title("Gui practice")
window.geometry("250x150")
window.resizable(0,False)


##label
user = Label (window, text = "name : ",fg="Black")
user.grid(row = 2, column = 0)

password = Label (window, text = "age : ",fg="Black")
password.grid(row = 10, column = 0)



##text feild
user_var = tkinter.StringVar()# to store value
user_entry = Entry(window)
user_entry.grid(row=2, column=2)

pass_var = tkinter.StringVar()
pass_entry = Entry(window)
pass_entry.grid(row=10, column=2)

# button
def login():
    user_obj = user_var.get()
    pass_obj = pass_var.get()
    print("you are doing great")

sumbit_btn = Button(window,text = "sumbit", command=login)
sumbit_btn.grid(row=60, column=2)


close_btn = Button(window,text = "Close",command = window.destroy)
close_btn.grid(row=90, column=2)
window.mainloop()