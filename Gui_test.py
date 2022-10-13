from  tkinter import*

window = Tk()
window.title("Gui practice")
window.geometry("250x150")
window.resizable(0,False)


##label
user = Label (window, text = "Username : ",fg="Black")
user.grid(row = 2, column = 0)

password = Label (window, text = "Password : ",fg="Black")
password.grid(row = 10, column = 0)



##text feild
user_lbl = Entry(window)
user_lbl.grid(row=2, column=2)

pass_lbl = Entry(window)
pass_lbl.grid(row=10, column=2)

# button
# login_btn = Button(window,text = "Login", command=window.login)
# login_btn.grid(row=60, column=2)

close_btn = Button(window,text = "Close",command = window.destroy)
close_btn.grid(row=90, column=2)
window.mainloop()