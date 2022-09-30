from tkinter import *
from tkinter.ttk import Combobox
from constants import *
from widgets.wid import SideButton, FlightFrame
from tkcalendar import DateEntry
import random as r
from utils import Frame_Base


class Nav(Frame):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        super().__init__(*args, **kwargs)

        self.init_buttons()
        self.place_widgets()

    def init_buttons(self):
        self.plane_btn = SideButton(master=self.kwargs.get("master", None), selected=1, img_path="images/flightimage.png", text="F", bg=self.kwargs.get("bg", "#ffffff"))

    def place_widgets(self):
        self.plane_btn.place(x=0, y=0, width=100, height=100)        


class Main_Frame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.placed = True

        self.trip_type = IntVar()

        self.flight_frame = Frame(master=self, bg="#ffffff")
        self.flight_frame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.4)
        
        self.create_flight_widgets()

        self.prev_w, self.prev_h = self.master.winfo_width(), self.master.winfo_height()
        self.master.bind_all("<Configure>", self.update_main_frame)


    def disable_return(self, type):
        if type == 0:
            self.ret_date_box.place_forget()
        elif type == 1:
            self.ret_date_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)


    def create_flight_widgets(self):
        ### TRIP TYPE WIDGET ###
        f_oneway_btn = Radiobutton(self.flight_frame, text="ONEWAY", value=1, font=(def_font, 10, "bold"), command=lambda: self.disable_return(0))
        f_oneway_btn.place(relx=0.03, rely=0.2, relwidth=0.15, relheight=0.1)
        
        f_roundtrip_btn = Radiobutton(self.flight_frame, text="ROUND TRIP", value=2, font=(def_font, 10, "bold"), command=lambda: self.disable_return(1))
        f_roundtrip_btn.place(relx=0.205, rely=0.2, relwidth=0.20, relheight=0.1)

        ### FROM WIDGET ###
        f_from_frame = Frame(self.flight_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#eeeeee", bd=10)
        f_from_frame.place(relx=0.03, rely=0.34, relwidth=0.25, relheight=0.34)

        from_lbl = Label(f_from_frame, text="FROM", bg="#ffffff", font=(def_font, 12, "bold")).place(relx=0.05, rely=0.1, relheight=0.2, width=50)

        ff_selection_box = Combobox(f_from_frame, values=cities, font=(def_font, 15, "bold"), state="readonly", name=0)
        ff_selection_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)

        ### TO WIDGET ###
        f_to_frame = Frame(self.flight_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#eeeeee", bd=10)
        f_to_frame.place(relx=0.28, rely=0.34, relwidth=0.2, relheight=0.34)

        to_lbl = Label(f_to_frame, text="TO", bg="#ffffff", font=(def_font, 12, "bold")).place(relx=0.05, rely=0.1, relheight=0.2, width=25)

        ft_selection_box = Combobox(f_to_frame, values=cities, font=(def_font, 15, "bold"), state="readonly", name=0)
        ft_selection_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)
        
        ### DEPARTURE WIDGET ###
        f_dep_frame = Frame(self.flight_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#eeeeee", bd=10)
        f_dep_frame.place(relx=0.48, rely=0.34, relwidth=0.175, relheight=0.34)

        dep_lbl = Label(f_dep_frame, text="DEPARTURE", bg="#ffffff", font=(def_font, 12, "bold")).place(relx=0.05, rely=0.1, relheight=0.2, width=100)

        dep_date_box = DateEntry(f_dep_frame, selectmode="day", font=(def_font, 12, "bold"))
        dep_date_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)
        
        ### RETURN WIDGET ###
        f_ret_frame = Frame(self.flight_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#eeeeee", bd=10)
        f_ret_frame.place(relx=0.655, rely=0.34, relwidth=0.15, relheight=0.34)

        self.ret_lbl = Label(f_ret_frame, text="RETURN", bg="#ffffff", font=(def_font, 12, "bold")).place(relx=0.05, rely=0.1, relheight=0.2, width=68)

        self.ret_date_box = DateEntry(f_ret_frame, selectmode="day", font=(def_font, 12, "bold"))
        self.ret_date_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)
        
        ### TRAVELLER WIDGET ###
        f_tra_frame = Frame(self.flight_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#eeeeee", bd=10)
        f_tra_frame.place(relx=0.805, rely=0.34, relwidth=0.175, relheight=0.34)
        tra_lbl = Label(f_tra_frame, text="TRAVELLERS", bg="#ffffff", font=(def_font, 12, "bold")).place(relx=0.05, rely=0.1, relheight=0.2, width=108)
        tra_box = Spinbox(f_tra_frame, font=(def_font, 12, "bold"), values=tuple(range(1,11)), state="readonly", highlightbackground="#ffffff", highlightthickness=0)
        tra_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)


        ### SEARCH BUTTON ###
        search_btn = Button(self.flight_frame, bg=LAVENDER, fg="#ffffff", text="Search", font=(def_font, 20, "bold"), bd=0, activebackground=LIGHT_LAVENDER, activeforeground="#ffffff")
        search_btn.place(relx=0.125*3, rely=0.8, relheight=0.15, relwidth=0.2)
        search_btn.bind("<ButtonRelease-1>", switch_frame)


    def update_main_frame(self, e=None):
        if not self.placed: return
        if e is None: 
            self.place(x=105, y=0, relheight=1, width=self.master.winfo_width()-105)
            return
        if e.width == self.prev_w and e.height == self.prev_h: return
        
        self.place(x=105, y=0, relheight=1, width=self.master.winfo_width()-105)
        self.prev_w, self.prev_h = e.width, e.height


class Display_Frame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.placed = False

        self.prev_w, self.prev_h = self.master.winfo_width(), self.master.winfo_height()
        self.master.bind_all("<Configure>", self.update_main_frame)

    def update_main_frame(self, e=None):
        if not self.placed: return
        if e is None: 
            self.place(x=105, y=0, relheight=1, width=self.master.winfo_width()-105)
            return
        if e.width == self.prev_w and e.height == self.prev_h: return
        
        self.place(x=105, y=0, relheight=1, width=self.master.winfo_width()-105)
        self.prev_w, self.prev_h = e.width, e.height


def main():
    global main_frame, flight_display_frame
    win = Tk()
    win.geometry(f"{WIDTH}x{HEIGHT}")
    win.minsize(WIDTH, HEIGHT)
    
    navbar = Nav(master=win, bg=NAV_BG)
    navbar.place(x=0, y=0, width=105, relheight=1)

    win.update()
    flight_display_frame = Display_Frame(master=win, bg="grey")
    main_frame = Main_Frame(master=win, bg=BG_COLOR)

    main_frame.update_main_frame()

    win.update()
    win.mainloop()


def switch_frame(e=None):
    global main_frame, flight_display_frame

    main_frame.place_forget()
    
    flight_display_frame.placed = True
    main_frame.placed = False

    flight_display_frame.update_main_frame()

def get_selected(navbar: Nav):
    for child in navbar.winfo_children():
        if child.label.cget("bg") == "#ffffff":
            return child.button["text"]

def get_oneway_flight_details():
    for i in range(10):
        flight_no = r.randint(100000, 999999)
        flight_name = r.choice()
        flight_start_time = r.randint(0, 23)
        flight_end_time = flight_start_time + r.randint(1, 6)
        flight_start_time = str(flight_start_time) + ":00"
        flight_end_time = str(flight_end_time) + ":00"
        flight_cost = r.randint(8000, 20000)

        yield flight_no, flight_name, flight_start_time, flight_end_time, flight_cost


if __name__ == "__main__":
    main()