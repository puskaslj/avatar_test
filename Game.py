from tkinter import *
from backend import Images
import glob
import itertools

Assets_dir = "All_Assets/"

base_list = glob.glob(Assets_dir+'*base*')
access_list = glob.glob(Assets_dir+'*access*')
background_list = glob.glob(Assets_dir+'*bg*')
eyes_list = glob.glob(Assets_dir+'*eyes*')
eyebrows_list = glob.glob(Assets_dir+'*brows*')
facialhair_list = glob.glob(Assets_dir+'*facial_hair*')
hair_list = glob.glob(Assets_dir+'*app_hair*')
mouth_list = glob.glob(Assets_dir+'*mouth*')
outfit_list = glob.glob(Assets_dir+'*outfit*')

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.base = PhotoImage(file = 'Bases/avatar_app_base_01.png')
        self.base_label = Label(master, image = self.base)
        self.base_label.grid(row = 0, column = 0, columnspan = 8, rowspan = 16, sticky = NE)
        
        

        #test buttons
        change_base = Button(master, text = "Change Base", width = 12, command = self.base_change)
        change_base.grid(row = 0, column = 9, sticky = E)

        change_eyes = Button(master, text = "Change Eyes", width = 12)
        change_eyes.grid(row = 0, column = 10, sticky = E)

        change_hair = Button(master, text = "Change Hair", width = 12)
        change_hair.grid(row = 1, column = 9, sticky = E)

    def base_change(self, base=base_list):
        self.next_base = itertools.cycle(base_list)
        self.new_base = next(self.next_base)
        self.base_label.configure(image = self.new_base)
        

root = Tk()
root.geometry("1000x600")
root.wm_title("Test")
app = Window(root)
root.mainloop()