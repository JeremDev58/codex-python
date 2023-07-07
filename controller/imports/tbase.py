import tkinter.ttk as ttk
import tkinter as tk


class TBase(ttk.Frame):
    def __init__(self, **kwargs):
        pass

    def _init_attr(self, kw) -> None:
        for k, v in kw.items():
            if k in list(self.__dict__.keys()) and isinstance(v, type(self.__dict__[k])):
                self.__dict__.update({k: v})
            else:
                if not isinstance(v, type(self.__dict__[k])):
                    raise TypeError("Attribute " + "'" + k + "'" + " is of type " + str(type(self.__dict__[k])) + ".")
                else:
                    raise KeyError("'" + k + "'" + " is not a attribute.") from None

    @staticmethod
    def hover_color(color='', bright=False, num=30) -> str:
        sub_color = color
        result = ''
        count = 0

        if color == '' or len(color) > 7:
            return color
        if '#' in color:
            sub_color = color[1:]

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
        return "#" + result
