from tkinter import *

def authenticate():
    if login_entry.get() == "Paulim" and password_entry.get() == "ghito98ki":
        result_label.config(text="Success", font=(9))
    else:
        result_label.config(text="Fail", font=(9))

window = Tk()
window.geometry('300x220')
window.title("Authentication")
window.config(bg="#98a4ff")

login_label = Label(window, text="Login:",font=("Times New Roman",12), bg="#98a4ff")
login_label.pack(pady=5)

login_entry = Entry(window, font=("Times New Roman",12), bg="#98a4ff", bd=0)
login_entry.pack(pady=5)

password_label = Label(window, text="Password:", font=("Times New roman",12), bg="#98a4ff")
password_label.pack(pady=5)

password_entry = Entry(window, show="*", font=("times NEw Roman", 12), bg="#98a4ff", bd=0)
password_entry.pack(pady=5)

authenticate_btn = Button(window, text="Accept", command=authenticate, font=("Times NEw Roman",12), bg="#b8c0ff", fg="black", bd=0)
authenticate_btn.pack(pady=10)
                  
result_label = Label(window, text="", font=("Times NEw ROman",12), bg="#98a4ff")
result_label.pack()

window.mainloop()
