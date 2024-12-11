from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()

win.geometry("750x250")


def submit():
    messagebox.showinfo("Success", "Submitted Successfully!")


# Creates top frame
frame1 = LabelFrame(win, width=400, height=180, bd=10,relief=RAISED)
frame1.pack()

# Stop the frame from propagating the widget to be shrink or fit
frame1.pack_propagate(False)

# Create an Entry widget in Frame1
entry1 = ttk.Entry(frame1, width=40)
entry1.insert(INSERT, "Enter Your Name")
entry1.pack(pady=30)
entry2 = ttk.Entry(frame1, width=40)
entry2.insert(INSERT, "Enter Your Email")
entry2.pack()

# Creates bottom frame for button
frame2 = LabelFrame(win, width=150, height=100,bg="red")
frame2.pack()

# Create a Button to enable frame
button1 = ttk.Button(frame2, text="Submit", command=submit)
button1.pack()

win.mainloop()
