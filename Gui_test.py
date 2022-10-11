from  tkinter import*
window = Tk()
window.title("Gui practice")
window.geometry("600x600")
window.resizable(0,False)

##label
user = Label (window, text = "Username : ",fg="Black")
user.grid(row = 0, column = 0)

password = Label (window, text = "Password : ",fg="Black")
password.grid(row = 6, column = 0)



##text feild
e1 = Entry(window)
e1.grid(row=0, column=2)

e2 = Entry(window)
e2.grid(row=6, column=2)

window.mainloop()