from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import *
import edit_menu
import file_menu
import format_menu

app = Tk()
app.title('I Text')
app.iconbitmap('icon.ico')
app.geometry('550x500')
app.minsize(width=350, height=300)
# Text Box
text_box = ScrolledText(app, width=500, height=500, wrap='word', pady=2, padx=3, undo=True)
text_box.pack(fill=Y, expand=1)
text_box.focus_set()

# Menu
app_menu = Menu(app)

file_menu.main(app, text_box, app_menu)
edit_menu.main(app, text_box, app_menu)
format_menu.main(app, text_box, app_menu)
app.mainloop()
