from views.view.view_new import *
from views.view.view_codex import *
from views.view.view_search import *
from views.models.menu_top import *
from views.models.menu_side import *
from audit import LST_FILES_REBUILD
from views.models.dialog_error import TLevel


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        style = ttk.Style()
        style.theme_create("test", "default", settings={
            "menu_top.TFrame": {"configure":
                                {"background": "#333333"}
                                },
            "menu_top.TButton": {"configure":
                                 {"background": "#333333",
                                  "selectbackground": "#ffffff",
                                  "foreground": "#d9534f",
                                  "width": 10},
                                 "map": {"background": [("selected", "#ffffff")]}
                                 },
            "view_codex.TButton": {"font": ("Orbitron", 75)},
            "Toolbutton" : {"configure":
                                  {"width": 100}}
        })
        # style.theme_use("test")
        # PARAMETRE PRINCIPALE
        self.geometry("800x550")
        self.title("Codex")
        self.search_category = {}
        self.search_custom = {}
        self.search_subtitle = {}
        self.search_title = {}
        self.search_tags = {}
        self.search_file = {}
        # DECLARATION
        try:
            for k, v in LST_FILES_REBUILD.items():
                data = {}
                with open(v, "r") as f:
                    if not f.read() == "":
                        data = json.loads(f.read())
                if k == "category.json":
                    self.search_category = data
                elif k == "custom_search.json":
                    self.search_custom = data
                elif k == "file.json":
                    self.search_file = data
                elif k == "subtitle.json":
                    self.search_subtitle = data
                elif k == "tags.json":
                    self.search_tags = data
                elif k == "title.json":
                    self.search_title = data
        except KeyError:
            pass
        except:
            TLevel(self, "Impossible de charger les fichiers search.\nLe logiciel doit être redémarrer.")

        self.menu_top = MenuTop(self)
        self.menu_side = SideMenu(self)
        self.view = TFrameScroll(self)


        # POSITIONNEMENT
        self.menu_top.pack(fill=tk.X)
        self.menu_side.pack(side=tk.LEFT, fill=tk.Y)
        self.view.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # COMMAND
        self.menu_top.btn_home.btn.configure(command=lambda: self.create_view(1))
        self.menu_side.btn_new_page.btn.configure(command=lambda: self.create_view(2))
        self.menu_top.btn_search.btn.configure(command=lambda: self.create_view())
        self.menu_side.btn_trash.btn["state"] = tk.DISABLED
        # self.menu_side.btn_new_page.btn["state"] = tk.DISABLED
        self.menu_side.btn_new_folder.btn["state"] = tk.DISABLED
        self.menu_top.btn_nxt.btn["state"] = tk.DISABLED
        self.menu_top.btn_prev.btn["state"] = tk.DISABLED


    def appear_scrollbar(self, event):
        if self.view.winfo_height() + self.menu_top().height > self.winfo_height():
            self.scrollbar = tk.Scrollbar(self)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        else:
            self.scrollbar.destroy()


    def create_view(self, view=0):
        self.view.destroy()
        if view == 1:
            self.view = ViewCodex(self)
            self.check_switch_view_codex()
        elif view == 2:
            self.view = TFrameScroll(self)
            self.check_switch_view_create()
        else:
            self.view = ViewSearch(self)
            self.check_switch_view_search()
        self.view.pack(fill=tk.BOTH, expand=True)

    def check_switch_view_codex(self):
        self.menu_side.btn_new_folder.btn["state"] = tk.ACTIVE
        pass

    def check_switch_view_search(self):
        pass

    def check_switch_view_create(self):
        pass

    def display_cdx(self):
        pass
