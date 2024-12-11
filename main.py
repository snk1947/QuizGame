from tkinter import *
from tkinter import font


class Main_Window:
    def __init__(self, master):
        self.root = master
        self.create_main_window()
        self.root.mainloop()

    def btn_local_pressed(self):
        print("LOKAL")
        self.window_local = Toplevel(self.root)
        cla_local_window = Local_Window(self.window_local, self.root)
        self.root.withdraw()

    def btn_remote_pressed(self):
        print("MASOFAVIY")
        self.window_remote = Toplevel(self.root)
        cla_remote_window = Remote_Window(self.window_remote)
        self.root.withdraw()

    def create_main_window(self):
        self.root_width = 500
        self.root_height = 350
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.loc_x = (self.screen_width - self.root_width) // 2
        self.loc_y = (self.screen_height - self.root_height) // 2 - 50
        self.root.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, self.loc_x, self.loc_y))
        self.root.resizable(False, False)
        self.root.title("Kirish qismi")
        self.clr_back = "lightgreen"
        self.root["bg"] = self.clr_back

        self.font_lbl = font.Font(family="Cambria", size=16, weight=font.BOLD, slant=font.ROMAN)
        self.font_btn = font.Font(family="Cambria", size=14, weight=font.BOLD, slant=font.ITALIC)

        self.lbl_title = Label(self.root, text="TESTNI ISHGA TUSHIRISH TURINI TANLANG", font=self.font_lbl,
                               bg=self.clr_back, relief=RIDGE, bd=4)
        self.lbl_title.place(relx=0.5, rely=0.15, anchor=CENTER, relwidth=0.9, relheight=0.15)

        self.btn_local = Button(self.root, text="MAHALLIY", font=self.font_btn, relief=GROOVE, bg="blue", fg="white",
                                activebackground="yellow", activeforeground="red", bd=6, command=self.btn_local_pressed)
        self.btn_local.place(relx=0.5, rely=0.45, anchor=CENTER, relwidth=0.4)
        self.btn_remote = Button(self.root, text="MASOFAVIY", font=self.font_btn, relief=GROOVE, bg="blue", fg="white",
                                 activebackground="yellow", activeforeground="red", bd=6,
                                 command=self.btn_remote_pressed)
        self.btn_remote.place(relx=0.5, rely=0.75, anchor=CENTER, relwidth=0.4)


class Local_Window:
    def __init__(self, master, root):
        self.window_local = master
        self.window_main = root
        self.create_local_window()

    def create_local_window(self):
        self.window_local.title("LOKAL rejimda test ishlash")
        self.window_local.geometry("1000x600")
        self.window_local.resizable(False, False)
        self.window_local.focus_set()
        # self.window_local.grab_set()
        self.btn_new = Button(self.window_local, text="TEST", command=self.window_main.deiconify)
        self.btn_new.pack(side=LEFT)


class Remote_Window:
    def __init__(self, master):
        self.window_remote = master
        self.create_remote_window()

    def create_remote_window(self):
        self.window_remote.title("MASOFAVIY rejimda test ishlash")
        self.window_remote.geometry("1000x600")
        self.window_remote.resizable(False, False)
        self.window_remote.focus()
        self.window_remote.grab_set()


window_main = Tk()

Main_Window(window_main)
