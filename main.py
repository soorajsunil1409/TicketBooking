from tkinter import *
from tkinter.ttk import Combobox
from constants import *
from widgets.wid import SideButton, NormalFlightFrame
from tkcalendar import DateEntry
import random as r


class Nav(Frame):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        super().__init__(*args, **kwargs)

        self.init_buttons()
        self.place_widgets()

    def init_buttons(self):
        self.plane_btn = SideButton(master=self.kwargs.get("master", None), selected=1, img_path="images/flightimage.png", text="F", bg=self.kwargs.get("bg", "#ffffff"))
        self.profile_btn = SideButton(master=self.kwargs.get("master", None), selected=1, img_path="images/flightimage.png", text="F", bg=self.kwargs.get("bg", "#ffffff"))
        self.plane_btn.bind_all("<Button-1>", switch_frame_to_home)

    def place_widgets(self):
        self.plane_btn.place(x=0, y=0, width=100, height=100)        


class Main_Frame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.placed = True
        self.ret = True

        self.trip_type = IntVar()

        self.flight_frame = Frame(master=self, bg="#ffffff")
        self.flight_frame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.4)
        
        self.create_flight_widgets()

        self.prev_w, self.prev_h = self.master.winfo_width(), self.master.winfo_height()


    def disable_return(self, type):
        if type == 0:
            self.ret = False
            self.ret_date_box.place_forget()
        elif type == 1:
            self.ret = True
            self.ret_date_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)


    def create_flight_widgets(self):
        ### TRIP TYPE WIDGET ###
        self.f_oneway_btn = Radiobutton(self.flight_frame, text="ONEWAY", value=1, font=(def_font, 10, "bold"), command=lambda: self.disable_return(0))
        self.f_oneway_btn.place(relx=0.03, rely=0.2, relwidth=0.15, relheight=0.1)
        
        self.f_roundtrip_btn = Radiobutton(self.flight_frame, text="ROUND TRIP", value=2, font=(def_font, 10, "bold"), command=lambda: self.disable_return(1))
        self.f_roundtrip_btn.place(relx=0.205, rely=0.2, relwidth=0.20, relheight=0.1)

        ### FROM WIDGET ###
        f_from_frame = Frame(self.flight_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#eeeeee", bd=10)
        f_from_frame.place(relx=0.03, rely=0.34, relwidth=0.25, relheight=0.34)

        from_lbl = Label(f_from_frame, text="FROM", bg="#ffffff", font=(def_font, 12, "bold")).place(relx=0.05, rely=0.1, relheight=0.2, width=50)

        self.ff_selection_box = Combobox(f_from_frame, values=cities, font=(def_font, 15, "bold"), state="readonly", name=0)
        self.ff_selection_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)

        ### TO WIDGET ###
        f_to_frame = Frame(self.flight_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#eeeeee", bd=10)
        f_to_frame.place(relx=0.28, rely=0.34, relwidth=0.2, relheight=0.34)

        to_lbl = Label(f_to_frame, text="TO", bg="#ffffff", font=(def_font, 12, "bold")).place(relx=0.05, rely=0.1, relheight=0.2, width=25)

        self.ft_selection_box = Combobox(f_to_frame, values=cities, font=(def_font, 15, "bold"), state="readonly", name=0)
        self.ft_selection_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)
        
        ### DEPARTURE WIDGET ###
        f_dep_frame = Frame(self.flight_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#eeeeee", bd=10)
        f_dep_frame.place(relx=0.48, rely=0.34, relwidth=0.175, relheight=0.34)

        dep_lbl = Label(f_dep_frame, text="DEPARTURE", bg="#ffffff", font=(def_font, 12, "bold")).place(relx=0.05, rely=0.1, relheight=0.2, width=100)

        self.dep_date_box = DateEntry(f_dep_frame, selectmode="day", font=(def_font, 12, "bold"))
        self.dep_date_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)
        
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
        self.tra_box = Spinbox(f_tra_frame, font=(def_font, 12, "bold"), values=tuple(range(1,11)), state="readonly", highlightbackground="#ffffff", highlightthickness=0)
        self.tra_box.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)


        ### SEARCH BUTTON ###
        self.search_btn = Button(self.flight_frame, bg=LAVENDER, fg="#ffffff", text="Search", font=(def_font, 20, "bold"), bd=0, activebackground=LIGHT_LAVENDER, activeforeground="#ffffff")
        self.search_btn.place(relx=0.125*3, rely=0.8, relheight=0.15, relwidth=0.2)
        self.search_btn.bind("<ButtonRelease-1>", self.switch)


    def switch(self, e=None):
        start_place = self.ff_selection_box.get()
        stop_place = self.ft_selection_box.get()
        start_date = self.dep_date_box._date
        stop_date = self.ret_date_box._date if self.ret else None
        travellers = self.tra_box.get()

        if not start_place or not stop_place or not start_date or not travellers: return

        main_frame_details = start_place, stop_place, travellers, start_date, stop_date

        switch_frame_to_display(main_frame_details)


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

    def initialize_flight_frames(self, main_frame_details):
        for child in self.winfo_children():
            child.destroy()

        flight_details = get_oneway_flight_details()
        tile_gap = 10
        tile_height = 100

        for i, single_flight_detail in enumerate(flight_details):
            frm = NormalFlightFrame(self, *single_flight_detail, *main_frame_details[:3])
            frm.place(relx=0.05, y=50+(i*tile_height) if i == 0 else 50+(i*tile_gap)+(i*tile_height), relwidth=0.9, height=tile_height)

    def update_frame(self, e=None):
        if not self.placed: return
        if e is None: 
            self.place(x=105, y=0, relheight=1, width=self.master.winfo_width()-105)
            return
        if e.width == self.prev_w and e.height == self.prev_h: return
        
        self.place(x=105, y=0, relheight=1, width=self.master.winfo_width()-105)
        self.prev_w, self.prev_h = e.width, e.height


def main():
    global main_frame, flight_display_frame, win
    win = Tk()
    win.geometry(f"{WIDTH}x{HEIGHT}")
    win.minsize(WIDTH, HEIGHT)
    
    navbar = Nav(master=win, bg=NAV_BG)
    navbar.place(x=0, y=0, width=105, relheight=1)

    win.update()
    flight_display_frame = Display_Frame(master=win, bg=LIGHT_LAVENDER)
    main_frame = Main_Frame(master=win, bg=BG_COLOR)
    
    win.bind_all("<Configure>", update_frames)

    win.update()
    win.mainloop()


def update_frames(e=None):
    flight_display_frame.update_frame()
    main_frame.update_main_frame()


def switch_frame_to_display(main_frame_details):
    global main_frame, flight_display_frame

    main_frame.place_forget()
    
    flight_display_frame.placed = True
    main_frame.placed = False

    flight_display_frame.initialize_flight_frames(main_frame_details)
    flight_display_frame.update_frame()


def switch_frame_to_home(e=None):
    if not isinstance(e.widget, Button) or e.widget["text"] != "F": return
    global main_frame, flight_display_frame

    flight_display_frame.place_forget()
    
    main_frame.placed = True
    flight_display_frame.placed = False

    main_frame.update_main_frame()


def get_selected(navbar: Nav):
    for child in navbar.winfo_children():
        if child.label.cget("bg") == "#ffffff":
            return child.button["text"]


def get_oneway_flight_details():
    for i in range(6):
        flight_no = "#"+str(r.randint(100000, 999999))
        flight_name = r.choice(flight_names)
        flight_start_time = r.randint(0, 23)
        flight_end_time = flight_start_time + r.randint(1, 6)
        flight_start_time = str(flight_start_time) + ":00"
        flight_end_time = str(flight_end_time) + ":00"
        flight_cost = r.randint(8000, 20000)

        yield flight_name, flight_no, flight_start_time, flight_end_time, flight_cost


if __name__ == "__main__":
    main()