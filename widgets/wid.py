from tkinter import *
from datetime import datetime

LBL_BG = "#8D86C9"
BORDER_COLOR = "#CDCDCD"
BG_COLOR = "#EEEEEE"

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
    def __init__(self, master, flight_name, flight_no, start_time, stop_time, price, start, stop, travellers, start_date, stop_date):
        super().__init__(master=master, bg="#ffffff")


        self.flight_name = flight_name
        self.flight_no = flight_no
        self.start_time = start_time
        self.stop_time = stop_time
        self.start = start
        self.stop = stop
        self.price = price
        self.travellers = travellers
        self.start_date = start_date
        self.stop_date = stop_date

        self.initialize()

    def initialize(self):
        # Flight Name and Number
        flight_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground=BORDER_COLOR, bd=10)
        flight_frm.place(x=0, y=0, relwidth=0.2, relheight=1)
        flight_lbl = Label(flight_frm, bg="#ffffff", text=self.flight_name, font=("Helvetica", 20, "bold"))
        flight_lbl.place(x=0, y=0, relwidth=1, relheight=0.8)
        flight_no_lbl = Label(flight_frm, fg="#444444", bg="#ffffff", text=self.flight_no, font=("Helvetica", 11))
        flight_no_lbl.place(x=0, rely=0.65, relwidth=1, relheight=0.25)

        # Start time and place
        start_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground=BORDER_COLOR, bd=10)
        start_frm.place(relx=0.2, y=0, relwidth=0.2, relheight=1)
        start_time_lbl = Label(start_frm, bg="#ffffff", text=self.start_time, font=("Helvetica", 20, "bold"))
        start_time_lbl.place(x=0, y=0, relwidth=1, relheight=0.8)
        start_place_lbl = Label(start_frm, fg="#444444", bg="#ffffff", text=self.start, font=("Helvetica", 11))
        start_place_lbl.place(x=0, rely=0.65, relwidth=1, relheight=0.25)

        # Total Time
        start, stop = int(self.start_time[-4::-1][::-1]), int(self.stop_time[-4::-1][::-1])
        total_time = stop - start if start < stop else stop+24 - start
        total_time = str(total_time) + "h 00m"
        stop_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground=BORDER_COLOR, bd=10)
        stop_frm.place(relx=0.4, y=0, relwidth=0.2, relheight=1)
        stop_time_lbl = Label(stop_frm, bg="#ffffff", text=total_time, font=("Helvetica", 15))
        stop_time_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Stop time and place
        stop_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground=BORDER_COLOR, bd=10)
        stop_frm.place(relx=0.6, y=0, relwidth=0.2, relheight=1)
        stop_time_lbl = Label(stop_frm, bg="#ffffff", text=self.stop_time, font=("Helvetica", 20, "bold"))
        stop_time_lbl.place(x=0, y=0, relwidth=1, relheight=0.8)
        stop_place_lbl = Label(stop_frm, fg="#444444", bg="#ffffff", text=self.stop, font=("Helvetica", 11))
        stop_place_lbl.place(x=0, rely=0.65, relwidth=1, relheight=0.25)

        # Price
        price_frm = Frame(self, bg="#ffffff", highlightthickness=1, highlightbackground=BORDER_COLOR, bd=10)
        price_frm.place(relx=0.8, y=0, relwidth=0.2, relheight=1)
        price_lbl = Label(price_frm, bg="#ffffff", text="₹"+str(self.price), font=("Helvetica", 20, "bold"))
        price_lbl.place(x=0, y=0, relwidth=1, relheight=0.7)
        self.view_more_btn = Button(price_frm, text="View More", font=("Helvetica", 12), bd=0, command=self.show_booking_page)
        self.view_more_btn.place(x=0, rely=0.7, relheight=0.3, relwidth=1)

    def show_booking_page(self):
        self.details = {
            "Travellers": self.travellers,
            "Flight_name": self.flight_name,
            "Flight_no": self.flight_no,
            "Start_Time": self.start_time,
            "Stop_Time" :self.stop_time,
            "From": self.start,
            "To" :self.stop,
            "Price": self.price,
            "Start_Date": self.start_date,
            "Stop_Date": self.stop_date
        }

        book = BookNowPage(self.master, self.details)
        book.grab_set()

class BookNowPage(Toplevel):
    def __init__(self, master, details):
        super().__init__(master=master, bg="#ffffff")

        self.details = details

        self.geometry("600x292")
        self.resizable(0, 0)

        self.initialize_widgets()

    def initialize_widgets(self):
        self.main_frame = Frame(self, highlightbackground=BORDER_COLOR, background=BG_COLOR, highlightthickness=1)
        self.main_frame.place(x=5, y=5, width=380, height=282)
        
        # region Details
        from_to_lbl = Label(self.main_frame, text=f"{self.details['From']}  →  {self.details['To']}", font=("Helvetica", 14, "bold"), anchor=W)
        from_to_lbl.place(x=5, y=0, relwidth=1, height=40)

        date = convert_to_date_format(self.details["Start_Time"], self.details["Stop_Time"], self.details["Start_Date"], self.details["Stop_Date"])
        dates = Label(self.main_frame, text=date, font=("Helvetica", 10), anchor=W)
        dates.place(x=5, y=40, relwidth=1, height=15)

        flight_name_lbl = Label(self.main_frame, text=f'{self.details["Flight_name"]}  {self.details["Flight_no"]}', font=("Helvetica", 12, "bold"), anchor=W)
        flight_name_lbl.place(x=5, y=70, relwidth=1, height=20)
        # endregion

        self.time_frame = Frame(self.main_frame, highlightbackground=BORDER_COLOR, background=BG_COLOR, highlightthickness=1)
        self.time_frame.place(x=5, y=100, width=365, height=85)

        self.baggage_frame = Frame(self.main_frame, highlightbackground=BORDER_COLOR, background=BG_COLOR, highlightthickness=1)
        self.baggage_frame.place(x=5, y=190, width=365, height=85)

        # region Baggage Details
        self.baggage_lbl = Label(self.baggage_frame, text='Baggage         Check-in         Cabin', font=("Helvetica", 13), anchor=W)
        self.baggage_lbl.place(x=5, y=5, relwidth=0.9, height=20)

        self.under_baggage_lbl1 = Label(self.baggage_frame, text='ADULT               15 Kgs (1            7 Kgs (1', font=("Helvetica", 11, "bold"), anchor=W)
        self.under_baggage_lbl1.place(x=5, y=30, relwidth=0.9, height=20)

        self.under_baggage_lbl2 = Label(self.baggage_frame, text='\t            piece only)         piece only)', font=("Helvetica", 11, "bold"), anchor=W)
        self.under_baggage_lbl2.place(x=5, y=50, relwidth=0.9, height=20)
        # endregion

        # region Time Details
        self.start_time_lbl = Label(self.time_frame, text=f'{self.details["Start_Time"]}        {self.details["From"]}', font=("Helvetica", 13, "bold"), anchor=W)
        self.start_time_lbl.place(x=5, y=5, relwidth=0.9, height=20)

        total_time = " ".join(date.split()[3:])
        self.total_time_lbl = Label(self.time_frame, text=f'\t      {total_time}', font=("Helvetica", 10), anchor=W, fg="#444444")
        self.total_time_lbl.place(x=5, y=30, relwidth=0.9, height=20)

        self.stop_time_lbl = Label(self.time_frame, text=f'{self.details["Stop_Time"]}        {self.details["To"]}', font=("Helvetica", 13, "bold"), anchor=W)
        self.stop_time_lbl.place(x=5, y=55, relwidth=0.9, height=20)
        # endregion

        fare_w = 215
        self.fare_frame = Frame(self, highlightbackground=BORDER_COLOR, background=BG_COLOR, highlightthickness=1)
        self.fare_frame.place(x=380, y=5, width=fare_w, height=282)

        # region Fare Details
        self.fare_title_lbl = Label(self.fare_frame, text="Fare Summary", font=("Helvetica", 15, "bold"), anchor=W)
        self.fare_title_lbl.place(x=10, y=10, width=fare_w-10, height=20)

        self.base_fare_lbl = Label(self.fare_frame, text="Base Fare", font=("Helvetica", 10, "bold"), anchor=W)
        self.base_fare_lbl.place(x=10, y=45, width=fare_w-10, height=10)

        base_fare_txt = f"Adult(s) ({self.details['Travellers']} x ₹{self.details['Price']})     ₹{int(self.details['Price']) * int(self.details['Travellers'])}"
        self.base_fare_price_lbl = Label(self.fare_frame, text=base_fare_txt, font=("Helvetica", 10), anchor=W)
        self.base_fare_price_lbl.place(x=10, y=60, width=fare_w-10, height=20)
        # endregion

def convert_to_date_format(start, stop, start_date, stop_date=None):
    start_time, stop_time = int(start[-4::-1][::-1]), int(stop[-4::-1][::-1])
    total_time = stop_time - start_time if start_time < stop_time else stop_time+24 - start_time

    month = start_date.strftime("%d %b, %Y")

    out = f"{month} {total_time}h 00m"
    return out


if __name__ == "__main__":

    def book_now():
        book = BookNowPage(win, None)
        book.grab_set()


    win = Tk()
    win.geometry("1000x600")
    win.config(bg="grey")

    Button(win, text="fddffdfd", command=book_now).pack()

    frm = NormalFlightFrame(win, "AirAsia", 184765, "01:00", "02:00", 23456, "Bengaluru", "Kochi", 2, datetime.now(), datetime.now())
    frm.place(x=105, y=100, height=100, width=1000-105)


    win.mainloop()
