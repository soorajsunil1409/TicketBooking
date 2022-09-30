from tkinter import *

LBL_BG = "#8D86C9"

class PlaceholderEntry(Entry):
    def __init__(self, placeholder="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs = kwargs
        self._placeholder = placeholder
        self.placeholder_fg= "#737373"

        self.set_placeholder()
        self.bind("<FocusIn>", self.on_click)
        self.bind("<FocusOut>", self.set_placeholder)

    def set_placeholder(self, e=None):
        if self.get(): return
        self["fg"] = self.placeholder_fg
        self.insert(0, self._placeholder)

    def on_click(self, e=None):
        if self.get() != self._placeholder or self["fg"] != self.placeholder_fg: return
        self["fg"] = self.kwargs.get("fg", "#000000")
        self.delete(0, "end")

class SideButton(Frame):
    def __init__(self, text="", selected=False, img_path="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs = kwargs

        self.font = ("Helvetica", 35, "bold")
        self.def_fg = "#bbbbbb"
        self.lbl_bg = "#F7ECE1"

        if img_path:
            self.img = PhotoImage(file=img_path)

        self.label = Label(self, bg=self.kwargs.get("bg", LBL_BG) if not selected else LBL_BG)
        self.label.place(x=0, y=0, width=5, height=100)

        self.button = Button(self, image=self.img if img_path else None, cursor="hand2", fg=LBL_BG, text=text, font=self.font, bd=0, bg=self.kwargs.get("bg", "#ffffff"), activebackground=self.kwargs.get("bg", "#000000"), activeforeground="#ffffff")
        self.button.place(x=5, y=0, width=95, relheight=1)
        self.button.bind("<Enter>", lambda e: e.widget.config(fg="#ffffff"))
        self.button.bind("<Leave>", lambda e: e.widget.config(fg=self.def_fg))
        self.button.bind("<ButtonRelease-1>", self.set_lbl_bg)

    def set_lbl_bg(self, e):
        childs: Frame = self.kwargs.get("master")

        for child in childs.winfo_children():
            if isinstance(child, SideButton):
                if child != self:
                    child.reset_lbl()
                else:
                    self.label.config(bg=LBL_BG)

    def reset_lbl(self):
        self.label.config(bg=self.kwargs.get("bg", "#ffffff"))

class NormalFlightFrame(Frame):
    def __init__(self, master, flight_name, flight_no, start_time, stop_time, price, start, stop, travellers):
        super().__init__(master=master, bg="#ffffff")

        self.travellers = travellers

        self.flight_name = flight_name
        self.flight_no = flight_no
        self.start_time = start_time
        self.stop_time = stop_time
        self.start = start
        self.stop = stop
        self.price = price

        self.initialize()

    def initialize(self):
        # Flight Name and Number
        flight_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground="#cdcdcd", bd=10)
        flight_frm.place(x=0, y=0, relwidth=0.2, relheight=1)
        flight_lbl = Label(flight_frm, bg="#ffffff", text=self.flight_name, font=("Helvetica", 20, "bold"))
        flight_lbl.place(x=0, y=0, relwidth=1, relheight=0.8)
        flight_no_lbl = Label(flight_frm, fg="#444444", bg="#ffffff", text=self.flight_no, font=("Helvetica", 11))
        flight_no_lbl.place(x=0, rely=0.65, relwidth=1, relheight=0.25)

        # Start time and place
        start_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground="#cdcdcd", bd=10)
        start_frm.place(relx=0.2, y=0, relwidth=0.2, relheight=1)
        start_time_lbl = Label(start_frm, bg="#ffffff", text=self.start_time, font=("Helvetica", 20, "bold"))
        start_time_lbl.place(x=0, y=0, relwidth=1, relheight=0.8)
        start_place_lbl = Label(start_frm, fg="#444444", bg="#ffffff", text=self.start, font=("Helvetica", 11))
        start_place_lbl.place(x=0, rely=0.65, relwidth=1, relheight=0.25)

        # Total Time
        start, stop = int(self.start_time[-4::-1][::-1]), int(self.stop_time[-4::-1][::-1])
        total_time = stop - start if start < stop else stop+24 - start
        total_time = str(total_time) + "h 00m"
        stop_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground="#cdcdcd", bd=10)
        stop_frm.place(relx=0.4, y=0, relwidth=0.2, relheight=1)
        stop_time_lbl = Label(stop_frm, bg="#ffffff", text=total_time, font=("Helvetica", 15))
        stop_time_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Stop time and place
        stop_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground="#cdcdcd", bd=10)
        stop_frm.place(relx=0.6, y=0, relwidth=0.2, relheight=1)
        stop_time_lbl = Label(stop_frm, bg="#ffffff", text=self.stop_time, font=("Helvetica", 20, "bold"))
        stop_time_lbl.place(x=0, y=0, relwidth=1, relheight=0.8)
        stop_place_lbl = Label(stop_frm, fg="#444444", bg="#ffffff", text=self.stop, font=("Helvetica", 11))
        stop_place_lbl.place(x=0, rely=0.65, relwidth=1, relheight=0.25)

        # Price
        price_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground="#cdcdcd", bd=10)
        price_frm.place(relx=0.8, y=0, relwidth=0.2, relheight=1)
        price_lbl = Label(price_frm, bg="#ffffff", text="₹"+str(self.price), font=("Helvetica", 20, "bold"))
        price_lbl.place(x=0, y=0, relwidth=1, relheight=1)



if __name__ == "__main__":
    win = Tk()
    win.geometry("1000x600")
    win.config(bg="grey")

    frm = NormalFlightFrame("AirAsia", 184765, "1:00", "02:00", "Bengaluru", "Kochi", 23456)
    frm.place(x=105, y=100, height=100, width=1000-105)

    win.mainloop()
