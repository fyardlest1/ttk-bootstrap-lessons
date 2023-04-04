import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window(title='Sizegrip', themename='flatly')
app.geometry('300x200')
app.resizable(True, True)

# grid layout
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

# create the sizegrip
sg = ttk.Sizegrip(app, bootstyle=DANGER)
sg.grid(row=1, sticky=S+E)

app.mainloop()


