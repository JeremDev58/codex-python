from controller.imports.Tbutton import TButton
import tkinter as tk
import tkinter.ttk as ttk
from views.models.dialog_error import TLevel


class ViewCodex(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master, style="view_codex.TFrame")
        self.win_master = master
        self.container_view = ttk.Frame(self, style="view_codex.TFrame")
        self.label_trace = ttk.Label(self, text="", style="view_codex.TLabel")
        self.tracker = []
        self.files_view = []
        self.cat_view = []
        self.label_trace.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        self.container_view.pack(fill=tk.BOTH, expand=1)
        self.display()

    def display(self):
        self.sort_cdx()
        self.display_cdx()

    def sort_cdx(self):
        if self.tracker:
            string_categories = ""
            for el in self.tracker:
                string_categories += el + "/"
            try:
                display_files = self.win_master.search_category[string_categories]
            except:
                TLevel(self.win_master, "Un Problème inattendue est survenu.\nLe logiciel doit être redémarrer.")
            for el in display_files:
                if el[-4:] == ".cdx":
                    self.files_view.append(el)
                    self.files_view.sort()
                else:
                    self.cat_view.append(el)
                    self.cat_view.sort()

    def display_cdx(self):
        icon_cat = u"\uf07b"
        icon_file = u"\uf15c"
        for el in self.cat_view:
            TButton(self.container_view, text=icon_cat, width=150, height=150, style="view_codex.TButton",
                   style_frame="view_codex_border.TFrame", padx=5, pady=5, label=el[0:-1]).pack(side=tk.LEFT,
                                                                               anchor=tk.NW, padx=10, pady=10)
        for el in self.files_view:
            TButton(self.container_view, text=icon_file, width=150, height=150, style="view_codex.TButton",
                    style_frame="view_codex_border.TFrame", padx=5, pady=5, label=self.win_master.search_title[el]).pack(side=tk.LEFT,
                                                                                                 anchor=tk.NW, padx=10,
                                                                                                 pady=10)

    def click_cat(self, name):
        name_category = name + "/"
        self.tracker.append(name_category)
        self.cat_view.clear()
        self.files_view.clear()
        self.container_view.destroy()
        self.container_view = ttk.Frame(self, style="view_codex.TFrame")
        self.container_view.pack(fill=tk.BOTH, expand=1)
        self.display()

    def click_file(self, title, name_file):
        self.tracker.append(title + ".cdx")
        self.cat_view.clear()
        self.files_view.clear()
        self.container_view.destroy()
        self.container_view = ttk.Frame(self, style="view_codex.TFrame")
        self.container_view.pack(fill=tk.BOTH, expand=1)
        try:
            with open(self.win_master.search_file[name_file], "r") as f:
                ttk.Label(self.container_view, text=f.read()).pack(fill=tk.BOTH, expand=1)
        except:
            TLevel(self.win_master, "Un Problème inattendue est survenu.\nLe logiciel doit être redémarrer.")