import os

from controller.imports.Tcontainer import TContainer
import tkinter as tk
from tkinter import ttk
import sys


# init attr sans verif
# self.__dict__.update((k, v) for k, v in kwargs.items() if k in list(self.__dict__.keys()))

# import os
#         if 'HOME' in os.environ: home = os.environ['HOME']
#         else: home = os.curdir
#         class_tcl = os.path.join(home, '.%s.tcl' % className)
#         class_py = os.path.join(home, '.%s.py' % className)
#         base_tcl = os.path.join(home, '.%s.tcl' % baseName)
#         base_py = os.path.join(home, '.%s.py' % baseName)

def isKey(d, key):
    try:
        d[key]
    except:
        return False
    return True


def insance(d, key, valeur, bool):
    if bool:
        return d[key]
    else:
        return valeur


def _r(win):
    children = win.winfo_children()

    for child in children:
        children.extend(child.winfo_children())

    return children


def check_style(**kwargs):
    background = insance(kwargs, "background", "#000000", isKey(kwargs, "background"))
    print(background)
    options = [("background", background), ("foreground", "#ffffff")]
    state_bg = [("pressed", "#d9d9d9"), ("!pressed", "#d9d9d9"), ("disabled", "#d9d9d9"), ("active", "#ececec")]
    state_fg = [("pressed", "#a0a0a0"), ("!pressed", "#000000"), ("disabled", "#a3a3a3"), ("active", "#a0a0a0")]
    return [options, {"background": state_bg}, {"foreground": state_fg}]


def bind_test_hover(event):
    geo = (event.widget.winfo_x(), event.widget.winfo_x() + event.widget.winfo_width(), event.widget.winfo_y(),
           event.widget.winfo_y() + event.widget.winfo_height())
    if (event.x > geo[1] or event.x < geo[0]) or (event.y > geo[3] or event.y < geo[2]):
        pass
    else:
        print("Dedans !")


def bind_test_hover_out(event):
    geo = (event.widget.winfo_x(), event.widget.winfo_x() + event.widget.winfo_width(), event.widget.winfo_y(),
           event.widget.winfo_y() + event.widget.winfo_height())
    if (event.x > geo[1] or event.x < geo[0]) or (event.y > geo[3] or event.y < geo[2]):
        print("Dehors !")


class Btn(ttk.Button):
    def __init__(self, master, **kwargs):
        ttk.Button.__init__(self, master=master, **kwargs)
        self.bind("<Enter>", self._hover)
        self.tk.call()

    def _hover(self, event):
        print("hover")


EVENT = ["<KeyPress>",
         "<Key>",
         "<KeyRelease>",
         "<ButtonPress>",
         "<Button>",
         "<ButtonRelease>",
         "<Motion>",
         "<Enter>",
         "<Leave>",
         "<FocusIn>",
         "<FocusOut>",
         "<Keymap>",
         "<Expose>",
         "<GraphicsExpose>",
         "<NoExpose>",
         "<Visibility>",
         "<Create>",
         "<Destroy>",
         "<Unmap>",
         "<Map>",
         "<MapRequest>",
         "<Reparent>",
         "<Configure>",
         "<ConfigureRequest>",
         "<Gravity>",
         "<ResizeRequest>",
         "<Circulate>",
         "<CirculateRequest>",
         "<Property>",
         "<SelectionClear>",
         "<SelectionRequest>",
         "<Selection>",
         "<Colormap>",
         "<ClientMessage>",
         "<Mapping>",
         "<VirtualEvent>",
         "<Activate>",
         "<Deactivate>",
         "<MouseWheel>"]

def test_scroll(event):
    print("Dans la fonction test_scroll")
    if event.widget.winfo_id == btr.winfo_id():
        if event.widget.state() != ():
            print("Changement d'état du bouton.")

# def _configure_interior(event):
#     # update the scrollbars to match the size of the inner frame
#     size = (canvas_frame.winfo_reqwidth(), canvas_frame.winfo_reqheight())
#     canvas.config(scrollregion="0 0 %s %s" % size)
#     if canvas_frame.winfo_reqwidth() != canvas.winfo_reqwidth():
#         # update the canvas's width to fit the inner frame
#         canvas.config(width=canvas_frame.winfo_reqwidth())


# def _configure_canvas(event):
#     if canvas_frame.winfo_reqwidth() != canvas.winfo_reqwidth():
#         # update the inner frame's width to fill the canvas
#         canvas.itemconfigure(canvas_frame_id, width=canvas.winfo_reqwidth())
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#     else:
#         scrollbar.pack_forget()


# def mouse_scroll(event):
#     # Fonction Test_yview
#     #
#     # Valeur Option1 moveto
#     # Valeur Option2 0.5746315789473684
#     if event.delta:
#         canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
#     else:
#         if event.num == 5:
#             move = 1
#         else:
#             move = -1
#
#         canvas.yview_scroll(move, "units")

def test_yview(option1, option2):
    print("Fonction Test_yview")
    print("Type Option1 " + str(type(option1)))
    print("Type Option2 " + str(type(option2)))
    print("Valeur Option1 " + str(option1))
    print("Valeur Option2 " + str(option2))

# i = 0
# def create_label():
#     global i
#     ttk.Label(canvas_frame, text="Label " + str(i)).pack(fill=tk.X)
#     i += 1

# j = -1
# def hide():
#     global j
#     global framescroll
#     if j == -1:
#         scrollbar.configure(command=canvas.yview)
#         canvas.configure(yscrollcommand=scrollbar.set)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         j += 1
#
#     if j == 0:
#         scrollbar.pack_forget()
#         j += 1
#     else:
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         j -= 1


def w_destroy(widget):
    widget.destroy()


if __name__ == "__main__":
    # GUI
    app = tk.Tk()
    print(app.bind_all())
    print(app.bind())
    print(app.event_info('<<NextWindow>>'))
    print(app.event_info('<<PrevWindow>>'))
    print(app.event_delete('<<NextWindow>>'))
    print(app.event_delete('<<PrevWindow>>'))
    print(app.bind_all())
    app.geometry("500x500")
    # style = ttk.Style()
    # style.configure("TFrame", background="#cd2468", pressed="#456465")
    # style.configure("IN.TFrame", background="#879521")
    # container = TContainer(app, pad_y=2, pad_x=2)
    # container.pack(anchor=tk.CENTER)
    #
    # style.configure("TLabel", background="#24ff75")
    #
    label2 = ttk.Label(app, text="Interior")
    label2.pack(padx=10, pady=10)
    #
    # container2 = TContainer(app, pad_y=2, pad_x=2)
    # container2.pack(padx=10, pady=10)

    style = ttk.Style()
    style.map("C.TButton",
              foreground=[('!active', 'black'), ('pressed', 'red'), ('active', 'white')],
              background=[('!active', 'grey75'), ('pressed', 'green'), ('active', 'black')]
              )

    style.map("C.TFrame",
              foreground=[('pressed', 'red'), ('active', 'white')],
              background=[('pressed', 'green'), ('active', 'black'), ('hover', 'pink'), ('selected', 'red')]
              )
    style.theme_use(None)
    frame = ttk.Frame(app, style="C.TFrame")
    frame.pack()
    frame.unbind("<Enter>")
    label3 = ttk.Label(frame, text="Label 3")
    label3.pack(padx=10, pady=10)
    btr = Btn(app, text="Hide")
    btr.pack()
    btn = tk.Button(app, text="Create Label")
    btn.pack()
    btn2 = tk.Button(app, text="BTN FLASH", command=lambda: w_destroy(app.children['!btn']), font=("Orbitron", 9))
    btn2.pack()
    varoption = tk.BooleanVar(value=True)
    boption = ttk.Checkbutton(app, text="dossiers", variable=varoption, onvalue=True, offvalue=False)
    boption.pack(fill=tk.X)

    # framescroll = ttk.Frame(app)
    # framescroll.pack(fill=tk.BOTH, expand=1)
    # canvas = tk.Canvas(framescroll)
    # canvas.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
    # scrollbar = ttk.Scrollbar(orient=tk.VERTICAL)
    # canvas_frame = ttk.Frame(canvas)
    #
    # canvas_frame_id = canvas.create_window((0, 0), window=canvas_frame, anchor="nw")
    # canvas_frame.bind("<Configure>", _configure_interior)
    # canvas.bind("<Configure>", _configure_canvas)
    #
    # canvas.event_add('<<wheel>>', '<Button-4>', '<Button-5>')
    # canvas.bind('<<wheel>>', mouse_scroll)
    cont = TContainer(app, pad_y=2, pad_x=2)
    cont.pack()

    lframe = ttk.Labelframe(app, text="test")
    lframe.pack()
    lab = ttk.Label(lframe, text="Test du labelframe en etat désactivé", font=("Orbitron", 12))
    lab.pack()
    esearch = tk.Text(lframe, font=("Orbitron", 12))
    esearch.pack(fill=tk.X)
    # for child in lframe.children.values():
    #     child["state"] = tk.DISABLED
    # esearch.insert(1.0, "COucou")
    c = esearch.get(0.0)
    children = app.winfo_children()
    for child in children:
        children.extend(child.winfo_children())
        try:
            child["state"] = 'disabled'
        except tk.TclError:
            pass
    print(app.children)


    app.mainloop()

    # CONSOLE

    # import os
    # import re
    #
    # rootdir = "/usr"
    # regex = re.compile('_tkinter')
    #
    # for root, dirs, files in os.walk(rootdir):
    #     for file in files:
    #         if regex.match(file):
    #             print(root + '/' + file + " -f")
    #     for directory in dirs:
    #         if regex.match(directory):
    #             print(root + '/' + directory + " -d")
    def OnKeyPress(event):
        value = event.widget.get()
        string = "value of %s is '%s'" % (event.widget._name, value)
        status.configure(text=string)


    root = tk.Tk()

    entry1 = tk.Entry(root, name="entry1")
    entry2 = tk.Entry(root, name="entry2")
    entry3 = tk.Entry(root, name="entry3")

    # Three different bindtags. The first is just the default but I'm
    # including it for illustrative purposes. The second reverses the
    # order of the first two tags. The third introduces a new tag after
    # the class tag.
    entry1.bindtags(('.entry1', 'Entry', '.', 'all'))
    entry2.bindtags(('Entry', '.entry2', '.', 'all'))
    entry3.bindtags(('.entry3', 'Entry', 'post-class-bindings', '.', 'all'))

    btlabel1 = tk.Label(text="bindtags: %s" % " ".join(entry1.bindtags()))
    btlabel2 = tk.Label(text="bindtags: %s" % " ".join(entry2.bindtags()))
    btlabel3 = tk.Label(text="bindtags: %s" % " ".join(entry3.bindtags()))
    status = tk.Label(anchor="w")

    entry1.grid(row=0, column=0)
    btlabel1.grid(row=0, column=1, padx=10, sticky="w")
    entry2.grid(row=1, column=0)
    btlabel2.grid(row=1, column=1, padx=10, sticky="w")
    entry3.grid(row=2, column=0)
    btlabel3.grid(row=2, column=1, padx=10)
    status.grid(row=3, columnspan=2, sticky="w")

    # normally you bind to the widget; in the third case we're binding
    # to the new bindtag we've created
    entry1.bind("<KeyPress>", OnKeyPress)
    entry2.bind("<KeyPress>", OnKeyPress)
    entry3.bind_class("post-class-bindings", "<KeyPress>", OnKeyPress)


    root.mainloop()