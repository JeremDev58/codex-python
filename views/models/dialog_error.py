import tkinter as tk
import tkinter.ttk as ttk


class TLevel(tk.Toplevel):
    def __init__(self, master, message):
        tk.Toplevel.__init__(self, master=master)
        self.resizable(0, 0)
        self.focus_set()
        self.grab_set()
        self.protocol('WM_DELETE_WINDOW', master.destroy)
        self.focus_force()
        self.title("Error")
    # Container Image
        self.container_img = ttk.Frame(self)
        self.logo = tk.PhotoImage(master=self.container_img, file="./fail.png")
        self.resize_logo = self.logo.subsample(4, 4)
        self.label_logo = ttk.Label(self.container_img, image=self.resize_logo)
        self.label_logo.pack(side=tk.TOP, pady=20)
        self.container_img.pack(side=tk.LEFT, fill=tk.Y)

    # Container Corps Window
        self.container_corps = ttk.Frame(self)
        self.label_tl_corps = ttk.Label(self.container_corps, text=message)
        self.btn_tl_close = tk.Button(self.container_corps, text="Fermer", command=lambda: master.destroy())
        self.container_corps.pack(side=tk.RIGHT)
        self.label_tl_corps.pack(padx=20, pady=30)
        self.btn_tl_close.pack(anchor=tk.SE)
