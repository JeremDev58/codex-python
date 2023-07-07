import tkinter.ttk as ttk
import tkinter as tk


class TButton(ttk.Frame):
    def __init__(self, master, text, width, height, style=None, style_frame=None, font=None, padx=None, pady=None,
                 command=None, label=None, style_label=None):
        ttk.Frame.__init__(self, master=master, width=width, height=height, style=style_frame)
        self.btn = ttk.Button(self, text=text, style=style, command=command)
        if label:
            self.label = ttk.Label(self, text=label, style=style_label)
            self.label.pack(side=tk.BOTTOM, fill=tk.X)
        if font:
            self.btn.configure(font=font)
        self.pack_propagate(0)
        if padx and pady:
            self.btn.pack(fill=tk.BOTH, expand=1, padx=padx, pady=pady)
        elif padx:
            self.btn.pack(fill=tk.BOTH, expand=1, padx=padx)
        elif pady:
            self.btn.pack(fill=tk.BOTH, expand=1, pady=pady)
        else:
            self.btn.pack(fill=tk.BOTH, expand=1)
