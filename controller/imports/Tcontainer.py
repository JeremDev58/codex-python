import tkinter.ttk as ttk
import tkinter as tk


class TContainer(ttk.Frame):
    _idcls = int()

    def __init__(self, master, **kwargs):
        """Construct a Ttk Frame within Ttk Frame.

                STANDARD OPTIONS

                    style_border, style_frame, pad_x, pad_y
        """
        # ATTR
        TContainer._idcls += 1
        self.style_border = "Default_Style_TContainer_Border_" + str(self._idcls) + ".TFrame"
        self.style_frame = ""
        self.pad_x = int()
        self.pad_y = int()
        self.bright = False
        self._children = []

        self._init_attr(kwargs)

        ttk.Frame.__init__(self, master=master, style=self.style_border)
        if self.style_border == "Default_Style_TContainer_Border_" + str(self._idcls) + ".TFrame":
            color_palette = self.check_style(self.winfo_class(), background="#202020")
            ttk.Style().configure(self["style"], background=color_palette[0], foreground=color_palette[1])
            ttk.Style().map(self["style"], background=[("pressed", color_palette[2]),
                                                        ("disabled", color_palette[3]),
                                                        ("active", color_palette[4]),
                                                        ("hover", color_palette[5])],
                            foreground=[("pressed", color_palette[6]),
                                        ("disabled", color_palette[7]),
                                        ("active", color_palette[8]),
                                        ("hover", color_palette[9])])

        self.interior = ttk.Frame(self, style=self.style_frame)
        if self.style_frame != "Default_Style_TContainer_Frame_" + str(self._idcls) + ".TFrame":
            self._bg_frame = ttk.Style().lookup(self.interior["style"], "background")
            self._bg_pressed_frame = ttk.Style().lookup(self.interior["style"], "pressed")
        else:
            ttk.Style().configure(self.style_frame, background="#e0e0e0")

        if self.pad_x and self.pad_y:
            self.interior.pack(padx=self.pad_x, pady=self.pad_y, fill=tk.BOTH, expand=1)
        elif self.pad_y:
            self.interior.pack(pady=self.pad_y, fill=tk.BOTH, expand=1)
        elif self.pad_x:
            self.interior.pack(padx=self.pad_x, fill=tk.BOTH, expand=1)
        else:
            self.interior.pack(fill=tk.BOTH, expand=1)

        self.lb = ttk.Label(self.interior, text='A ma vie de coer entier')
        self.lb.pack(padx=10, pady=10)
        self._bind_recursive()
        self.bind("<Enter>", self._hover)
        self.bind("<Leave>", self._hover_out)
        self.bind("<Button-1>", self._press_in)
        self.bind("<ButtonRelease-1>", self._press_release)

    def _init_attr(self, kw) -> None:
        for k, v in kw.items():
            if k in list(self.__dict__.keys()) and isinstance(v, type(self.__dict__[k])):
                self.__dict__.update({k: v})
            else:
                if not isinstance(v, type(self.__dict__[k])):
                    raise TypeError("Attribute " + "'" + k + "'" + " is of type " + str(type(self.__dict__[k])) + ".")
                else:
                    raise KeyError("'" + k + "'" + " is not a attribute.") from None

    def _hover(self, event) -> None:
        self.state(['hover'])
        for child in self._children:
            child.state(["hover"])
            print(child.state())

    def _hover_out(self, event) -> None:
        geo = (event.widget.winfo_x(), event.widget.winfo_x() + event.widget.winfo_width(), event.widget.winfo_y(),
               event.widget.winfo_y() + event.widget.winfo_height())
        if (event.x > geo[1] or event.x < geo[0]) or (event.y > geo[3] or event.y < geo[2]):
            self.state(['!hover'])
            for child in self._children:
                child.state(['!hover'])

    def _press_in(self, event) -> None:
        self.state(['pressed'])
        for child in self._children:
            child.state(["pressed"])

    def _press_release(self, event) -> None:
        self.state(['!pressed'])
        for child in self._children:
            child.state(["!pressed"])

    def _bind_recursive(self):
        children = self.winfo_children()
        for child in children:
            children.extend(child.winfo_children())
            if child["style"] != '':
                color_palette = self.check_style(child["style"])
            else:
                color_palette = self.check_style(child.winfo_class())
            # Verifier que c'est un objet ttk et sinon géré les objet tk car ils n'ont pas l'attribut "style".
            child["style"] = str(child.winfo_id()) + "." + child.winfo_class()
            ttk.Style().configure(child["style"], background=color_palette[0], foreground=color_palette[1])
            print("color_palette size: " + str(len(color_palette)))
            ttk.Style().map(child["style"], background=[("pressed", color_palette[2]),
                                                        ("disabled", color_palette[3]),
                                                        ("active", color_palette[4]),
                                                        ("hover", color_palette[5])],
                            foreground=[("pressed", color_palette[6]),
                                        ("disabled", color_palette[7]),
                                        ("active", color_palette[8]),
                                        ("hover", color_palette[9])])
            child.unbind("<Enter>")
            child.unbind("<Leave>")
            self._children.append(child)

    def rebind(self):
        self._bind_recursive()

    def check_style(self, style, **kwargs):
        background = self.instance(kwargs, "background", "#d9d9d9", self.is_key(kwargs, "background"))
        foreground = self.instance(kwargs, "foreground", "#000000", self.is_key(kwargs, "foreground"))
        options = [("background", "#d9d9d9"), ("foreground", "#000000")]
        state_bg = [("pressed", "#d9d9d9"), ("disabled", "#d9d9d9"), ("active", "#ececec"), ("hover", "#d9d9d9")]
        state_fg = [("pressed", "#000000"), ("disabled", "#a3a3a3"), ("active", "#000000"), ("hover", "#000000")]
        result = []

        if ttk.Style().lookup(style, options[0][0]) == options[0][1]:
            result.append(background)
        else:
            result.append(ttk.Style().lookup(style, options[0][0]))
        if ttk.Style().lookup(style, options[1][0]) == options[1][1]:
            result.append(foreground)
        else:
            result.append(ttk.Style().lookup(style, options[1][0]))
        # Background Color
        hover_color_bg = self.hover_color(result[0], self.bright)
        # Pressed
        if ttk.Style().lookup(style, options[0][0], state=[state_bg[0][0]]) == state_bg[0][1]:
            result.append(self.hover_color(hover_color_bg, self.bright))
        else:
            result.append(ttk.Style().lookup(style, options[0][0], state=[state_bg[0][0]]))
        # Disabled
        if ttk.Style().lookup(style, options[0][0], state=[state_bg[1][0]]) == state_bg[1][1]:
            result.append(result[2])
        else:
            result.append(ttk.Style().lookup(style, options[0][0], state=[state_bg[1][0]]))
        # Active
        if ttk.Style().lookup(style, options[0][0], state=[state_bg[2][0]]) == state_bg[2][1]:
            result.append(hover_color_bg)
        else:
            result.append(ttk.Style().lookup(style, options[0][0], state=[state_bg[2][0]]))
        # Hover
        if ttk.Style().lookup(style, options[0][0], state=[state_bg[3][0]]) == state_bg[3][1]:
            result.append(hover_color_bg)
        else:
            result.append(ttk.Style().lookup(style, options[0][0], state=[state_bg[3][0]]))
        # Foreground
        hover_color_fg = self.hover_color(result[0], self.bright)
        # Pressed
        if ttk.Style().lookup(style, options[1][0], state=[state_fg[0][0]]) == state_fg[0][1]:
            result.append(self.hover_color(hover_color_fg, self.bright))
        else:
            result.append(ttk.Style().lookup(style, options[1][0], state=[state_fg[0][0]]))
        # Disabled
        if ttk.Style().lookup(style, options[1][0], state=[state_fg[1][0]]) == state_fg[1][1]:
            result.append(result[6])
        else:
            result.append(ttk.Style().lookup(style, options[1][0], state=[state_fg[1][0]]))
        # Active
        if ttk.Style().lookup(style, options[1][0], state=[state_fg[2][0]]) == state_fg[2][1]:
            result.append(hover_color_fg)
        else:
            result.append(ttk.Style().lookup(style, options[1][0], state=[state_fg[2][0]]))
        # Hover
        if ttk.Style().lookup(style, options[1][0], state=[state_fg[3][0]]) == state_fg[3][1]:
            result.append(hover_color_fg)
        else:
            result.append(ttk.Style().lookup(style, options[1][0], state=[state_fg[3][0]]))

        return result

    @staticmethod
    def hover_color(color='', bright=False, num=30) -> str:
        sub_color = color
        result = ''
        count = 0

        if color == '' or len(color) > 7:
            return color
        if '#' in color:
            sub_color = color[1:]
            if len(sub_color) != 6:
                return color
        if len(color) < 6:
            return color

        while count < len(sub_color):
            if bright:
                color_int = int(sub_color[count:count + 2], 16) + num
                if color_int > 255:
                    color_int = 255
            else:
                color_int = int(sub_color[count:count + 2], 16) - num
                if color_int < 0:
                    color_int = 0
            color_hex = hex(color_int)[2:]
            if len(color_hex) != 2:
                color_hex = "0" + color_hex
            result += color_hex
            count += 2
        if result == sub_color:
            result = TContainer.hover_color(color, True, num)
        if "#" in result:
            return result
        else:
            return "#" + result

    @staticmethod
    def is_key(dictionary, key):
        try:
            dictionary[key]
        except KeyError:
            return False
        return True

    @staticmethod
    def instance(dictionary, key, value, boolean):
        if boolean:
            return dictionary[key]
        else:
            return value
