from controller.imports.Tbutton import TButton
import tkinter as tk
import tkinter.ttk as ttk

ORBITRON_FONT_XL = ("Orbitron", 17)
ORBITRON_FONT_M = ("Orbitron", 10)


class ViewSearch(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master, style="view_search.TFrame")

        # Déclaration du titre
        self.container_search = ttk.Frame(self, style="view_search.TFrame")
        self.title = ttk.Label(self.container_search, text="Recherche", font=ORBITRON_FONT_XL,
                               style="view_search.TLabel")

        # Déclaration de la recherche par titre & sous-titre
        self.container_title = ttk.Frame(self, style="view_search.TFrame")
        self.main_search_title = ttk.Label(self.container_title, text="Title", font=ORBITRON_FONT_M,
                                           style="view_search.TLabel")
        self.main_search_title_entry = ttk.Entry(self.container_title, exportselection=0)
        self.main_search_sb = ttk.Label(self.container_title, text="Sub-Title", font=ORBITRON_FONT_M,
                                        style="view_search.TLabel")
        self.main_search_sb_entry = ttk.Entry(self.container_title, exportselection=0)

        # Déclaration de la recherche par tag
        self.container_tag = ttk.Frame(self, style="view_search.TFrame")
        self.main_search_tag = ttk.Label(self.container_tag, text="Tags", font=ORBITRON_FONT_M,
                                         style="view_search.TLabel")
        self.tag_select = tk.StringVar
        self.tags = ["Exemple", "pour", "le", "prototype"]
        self.main_search_list_tags = ttk.Combobox(self.container_tag, textvariable=self.tag_select, values=self.tags,
                                                  state='readonly')
        # Déclaration de la recherche perso
        self.container_search_perso = ttk.LabelFrame(self, text="Recherche personalisé",
                                                     style="view_search.TLabelframe")
        self.content_select = tk.StringVar
        self.contents = ["Exemple", "pour", "le", "prototype"]
        self.search_perso_list = ttk.Combobox(self.container_search_perso, textvariable=self.content_select,
                                              values=self.contents, state='readonly')
        self.search_perso_entry = ttk.Entry(self.container_search_perso, exportselection=0)
        self.btn_submit = ttk.Button(self, text="Rechercher", style="view.TButton")

        # Positionnement
        self.title.pack(side=tk.LEFT, padx=10)
        self.main_search_title.pack(side=tk.LEFT, padx=10)
        self.main_search_title_entry.pack(side=tk.LEFT, fill=tk.X, expand=1, padx=10)
        self.main_search_sb.pack(side=tk.LEFT, padx=10)
        self.main_search_sb_entry.pack(side=tk.LEFT, fill=tk.X, expand=1, padx=10)
        self.main_search_tag.pack(side=tk.LEFT, padx=10)
        self.main_search_list_tags.pack(side=tk.LEFT, padx=10)
        self.search_perso_list.pack(side=tk.LEFT, padx=10)
        self.search_perso_entry.pack(side=tk.LEFT, fill=tk.X, expand=1, padx=10)
        self.container_search.pack(fill=tk.BOTH, expand=1)
        self.container_title.pack(fill=tk.BOTH, expand=1)
        self.container_tag.pack(fill=tk.BOTH, expand=1)
        self.container_search_perso.pack(fill=tk.BOTH, expand=1)
        self.btn_submit.pack(side=tk.RIGHT)
