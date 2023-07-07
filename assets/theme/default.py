import tkinter.ttk as ttk
{"menu_top": {
    "background": "#333333",
    "foreground": "#d9534f",
    "bg_disabled": "#333333",
    "bg_focus": "#414141",
    "bg_active": "#414141"
            },
"menu_side": {
    "background": "#444444",
    "foreground": "#d9534f",
    "bg_disabled": "#333333",
    "bg_focus": "#414141",
    "bg_active": "#414141"
},
"views": {
    "background": "#555555",
    "foreground": "#ebf0f0",
    "bg_disabled": "#555555",
    "bg_focus": "#d9534f",
    "bg_active": "#d9534f",
    "fg_disabled": "",
    "fg_focus": "#d9534f",
    "fg_active": "#d9534f"
},
"font": "Orbitron",
"font_size": {
    "h1": "20",
    "h2": "17",
    "h3": "15",
    "h4": "12",
    "current": "10"
}
}


ttk.Style().configure(".", font=("Orbitron", 10))
ttk.Style().configure("TLabel", relief="flat", foreground="#ebf0f0")
ttk.Style().configure("TButton", relief="flat", font=("Orbitron", 15))
ttk.Style().configure("menu_top.TFrame", background="#333333")
ttk.Style().configure("menu_top.TButton", background="#333333", foreground="#d9534f", width=10)
ttk.Style().map("menu_top.TButton", background=[("disabled", "#333333"), ("focus", "#414141"),
                                                ("active", "#414141")])
ttk.Style().configure("menu_top.TLabel", background="#333333")
ttk.Style().configure("menu_side.TFrame", background="#444444")
ttk.Style().configure("menu_side.TButton", background="#444444", foreground="#d9534f")
ttk.Style().map("menu_side.TButton", background=[("disabled", "#444444"), ("focus", "#333333"),
                                                 ("active", "#333333")])
ttk.Style().configure("view_search.TFrame", background="#555555")
ttk.Style().configure("view_search.TButton", background="#555555", foreground="#ebf0f0")
ttk.Style().configure("view_search.TLabelframe", background="#555555", foreground="#ebf0f0")
ttk.Style().configure("view_search.TLabel", background="#555555")

ttk.Style().configure("view_codex.TFrame", background="#555555")
ttk.Style().configure("view_codex_border.TFrame", background="#555555")
ttk.Style().map("view_codex_border.TFrame", background=[("focus", "#d9534f"), ("active", "#d9534f")])
ttk.Style().configure("view_codex.TButton", font=(None, 80), foreground="#ebf0f0", background="#555555")
ttk.Style().map("view_codex.TButton", foreground=[("focus", "#d9534f"), ("active", "#d9534f")],
                background=[("focus", "#444444"), ("active", "#555555")])

ttk.Style().configure("view_create.TEntry", font=("Orbitron", 15))
