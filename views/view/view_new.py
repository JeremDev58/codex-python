import tkinter as tk
import tkinter.ttk as ttk
from controller.imports.Tbutton import TButton
from controller.imports.font_select import FontSelectFrame

class TFrameScroll(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master)
        """
            Créer un menu pour les font.
        """
        self.menu_font_container = ttk.Frame(self)
        self.menu_font_container.pack(side=tk.TOP, fill=tk.X)
        self.menu_font = MenuText(self.menu_font_container)
        self.menu_font.pack(anchor=tk.CENTER)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        self.interior = ViewCreate(self.canvas)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor=tk.NW)

        self.event_add('<<wheel>>', '<Button-4>', '<Button-5>')
        self.interior.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)
        self.bind(self, "<MouseWheel>", self.mouse_scroll)
        self.bind(self, "<<wheel>>", self.mouse_scroll)

    def _configure_interior(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canvas.config(width=self.interior.winfo_reqwidth())

    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # update the inner frame's width to fill the canvas
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())

    def mouse_scroll(self, evt):
        if evt.state == 0:
            self.canvas.yview_scroll(int(evt.delta / 120), 'units')  # For windows
        if evt.state == 1:
            self.canvas.xview_scroll(int(evt.delta / 120), 'units')  # For windows


class ViewCreate(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master=master)
        self.box_plus = None
        self.name_file = None
        # A faire pour limitée le nombre de boite
        self.box_open = None
        self.box_validate = None
        # ---------------------------------------
        self.box_title = ttk.LabelFrame(self, text="Titre")
        content_entry = tk.StringVar
        self.entry_title = ttk.Entry(self.box_title, textvariable=content_entry, style="view_create.TEntry")
        self.entry_title.bind("<Return>", self.on_pressed_enter)
        self.box_title.pack(side=tk.TOP, fill=tk.X, pady=15, padx=10)
        self.entry_title.pack(fill=tk.X, padx=20, pady=10)
        self.create_box_plus()

    def create_box_plus(self):
        self.box_plus = BoxPlus(self)
        self.box_plus.pack(side=tk.TOP, fill=tk.X, pady=15, padx=10)

    def create_box_label(self, text, master):
        TButton(master, width=20, height=20, text=u"\uf014").pack(side=tk.RIGHT, padx=10)
        TButton(master, text=u"\uf044", height=10, width=10).pack(side=tk.RIGHT, padx=10)
        label_container = ttk.Frame(master)
        label_container.pack(fill=tk.BOTH, expand=1)
        fl = ttk.Label(label_container, text=text, font=('Lohit Tamil', 11))
        print(master.master.master.master.menu_font.font.font[0])
        fl.pack(anchor=tk.CENTER, padx=20, pady=10)



    def on_pressed_enter(self, event):
        name_file = event.widget.get()
        # self.create_file_cdx(self.name_file)
        event.widget.destroy()
        self.box_plus.destroy()
        self.create_box_label(name_file, event.widget.master)
        self.box_plus = BoxPlus(self)
        self.box_plus.pack(fill=tk.X)
        self.box_plus.btn['state'] = tk.NORMAL

    def create_box(self, name):
        container = ttk.LabelFrame(self, text=name)
        self.box_plus.destroy()
        if name == "SubTitle":
            content_entry = tk.StringVar
            entry = ttk.Entry(container, textvariable=content_entry, style="view_create.TEntry")
            entry.bind("<Return>", self.on_pressed_enter)
            entry.pack(fill=tk.X, padx=20, pady=10)
        elif name == "Text":
            content_msg = tk.StringVar
            msg = tk.Text(container)
            msg.bind("<Return>", self.on_pressed_enter)
            msg.pack(fill=tk.X, padx=20, pady=10)
        else:
            content_entry = tk.StringVar
            entry = ttk.Entry(container, textvariable=content_entry, style="view_create.TEntry")
            entry.pack(fill=tk.X, padx=20, pady=10)
            content_msg = tk.StringVar
            msg = tk.Message(container, textvariable=content_msg)
            msg.bind("<Return>", self.on_pressed_enter)
            msg.pack(fill=tk.X, padx=20, pady=10)
        container.pack(side=tk.TOP, fill=tk.X, pady=15, padx=10)
        self.create_box_plus()
        self.box_plus.btn['state'] = tk.DISABLED


class BoxPlus(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master=master)
        self.btn = tk.Menubutton(self, text="+", relief=tk.RAISED, font=("Obtitron", 20))
        self.btn.menu = tk.Menu(self.btn, tearoff=0)
        self.btn["menu"] = self.btn.menu
        self.btn.menu.add_command(label="SubTitle", command=lambda: self.master.create_box("SubTitle"))
        self.btn.menu.add_command(label="Text", command=lambda: self.master.create_box("Text"))
        self.btn.menu.add_command(label="Custom", command=lambda: self.master.create_box("Custom"))
        self.btn.pack(anchor=tk.CENTER, pady=10)


class MenuText(ttk.Frame):
    def __init__(self, master):
        self.font_attr = None
        ttk.Frame.__init__(self, master)
        self.align = ttk.Frame(self)
        self.align.pack(side=tk.LEFT)

        self.btn_align_left = TButton(self.align, text=u"\uf036", padx=5, pady=5, width=38, height=38)
        self.btn_align_left.pack(side=tk.LEFT)
        self.btn_align_middle = TButton(self.align, text=u"\uf039", padx=5, pady=5, width=38, height=38)
        self.btn_align_middle.pack(side=tk.LEFT)
        self.btn_align_right = TButton(self.align, text=u"\uf038", padx=5, pady=5, width=38, height=38)
        self.btn_align_right.pack(side=tk.LEFT)

        self.font = FontSelectFrame(self, fontsize=10)
        self.font.pack(side=tk.LEFT)






