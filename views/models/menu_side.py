from controller.imports.Tbutton import TButton
import tkinter as tk
import tkinter.ttk as ttk


class SideMenu(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master, style="menu_side.TFrame")
        self.btn_new_page = TButton(self, width=50, height=50, text=u"\uf15b", style="menu_side.TButton")
        self.btn_new_folder = TButton(self, width=50, height=50, text=u"\uf07b", style="menu_side.TButton")
        self.btn_trash = TButton(self, width=50, height=50, text=u"\uf014", style="menu_side.TButton")

        self.btn_new_page.pack(side=tk.TOP)
        self.btn_new_folder.pack(side=tk.TOP)
        self.btn_trash.pack(side=tk.TOP)
