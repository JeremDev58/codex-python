from controller.imports.Tbutton import TButton
import tkinter as tk
import tkinter.ttk as ttk


class MenuTop(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master, height=100, style="menu_top.TFrame")
        self.btn_prev = TButton(self, width=50, height=50, text=u"\uf060", style="menu_top.TButton")
        self.btn_nxt = TButton(self, width=50, height=50, text=u"\uf061", style="menu_top.TButton")
        self.btn_home = TButton(self, width=50, height=50, text=u"\uf015", style="menu_top.TButton")
        self.btn_search = TButton(self, width=50, height=50, text=u"\U0001F50D", style="menu_top.TButton")
        self.logo = tk.PhotoImage(master=self, file="./assets/theme/images/Codex.png")
        self.resize_logo = self.logo.subsample(4, 4)
        self.label_logo = ttk.Label(self, image=self.resize_logo, style="menu_top.TLabel")
        self.btn_settings = TButton(self, width=50, height=50, text=u"\uf013", style="menu_top.TButton")

        self.btn_prev.pack(side=tk.LEFT)
        self.btn_nxt.pack(side=tk.LEFT)
        self.btn_home.pack(side=tk.LEFT)
        self.btn_search.pack(side=tk.LEFT)
        # self.label_logo.pack(side=tk.LEFT, expand=1)
        self.btn_settings.pack(side=tk.RIGHT)
