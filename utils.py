from tkinter import *

class Frame_Base(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.prev_w, self.prev_h = self.master.winfo_width(), self.master.winfo_height()
        self.master.bind("<Configure>", self.update_main_frame)
        

    def update_main_frame(self, e=None):
        print(self.placed)
        if e is None: 
            self.place(x=105, y=0, relheight=1, width=self.master.winfo_width()-105)
            return
        if e.width == self.prev_w and e.height == self.prev_h: return
        
        self.place(x=105, y=0, relheight=1, width=self.master.winfo_width()-105)
        self.prev_w, self.prev_h = e.width, e.height