from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families
from tkinter.scrolledtext import *

import time
import sys

class Format():
    def __init__(self, text):
        self.text = text

    def IT_Light(self):
        self.text.config(bg='#ffffff', fg='#000000', selectbackground='#add5fa', selectforeground='#000000')
    def IT_LightP(self):
        self.text.config(bg='#ffffff', fg='#267f99', selectbackground='#add5fa', selectforeground='#267f99')
    def IT_Dark(self):
        self.text.config(bg='#1e1e1e', fg='#f0f0f0', selectbackground='#264f78', selectforeground='#f0f0f0')
    def IT_DarkP(self):
        self.text.config(bg='#1e1e1e', fg='#4ec9b0', selectbackground='#264f78', selectforeground='#4ec9b0')
    def monokai(self):
        self.text.config(bg='#272822', fg='#a6e22e', selectbackground='#575a5a', selectforeground='#a6e22e')
def main(root, textbox, menubar):

    objFormat = Format(textbox)

    scrollbar = Scrollbar(menubar)
    fontoptions = families(root)
    font = Font(family="arial", size=18)
    textbox.configure(font=font)

    format_menu = Menu(menubar, tearoff=False)

    font_submenu = Menu(menubar, tearoff=False)
    for option in fontoptions:
        font_submenu.add_command(label=option, command=lambda option=option: font.configure(family=option))
        font_submenu.config()
    size_submenu = Menu(menubar, tearoff=False)
    size_list = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
    for value in size_list:
        size_submenu.add_command(label=str(value), command=lambda value=value: font.configure(size=value))

    theme_menu = Menu(menubar, tearoff=False)
    format_menu.add_cascade(label='Theme', menu=theme_menu)
    theme_menu.add_command(label="IT Light", command=objFormat.IT_Light, accelerator="(default I Text)")
    theme_menu.add_command(label="IT Light+", command=objFormat.IT_LightP, accelerator="(default I Text)")
    theme_menu.add_separator()
    theme_menu.add_command(label="IT Dark", command=objFormat.IT_Dark, accelerator="(default I Text)")
    theme_menu.add_command(label="IT Dark+", command=objFormat.IT_DarkP, accelerator="(default I Text)")
    theme_menu.add_command(label="Monokai", command=objFormat.monokai, accelerator="")
    format_menu.add_cascade(label='Font', menu=font_submenu)
    format_menu.add_cascade(label='Size', menu=size_submenu)
    menubar.add_cascade(label="Format", menu=format_menu)


    root.config(menu=menubar)
