from tkinter import Entry, Frame, Button, Label, PhotoImage
from constants import LBL_BG

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

class FlightFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
