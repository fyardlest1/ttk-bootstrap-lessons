import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window(title='Paned Window', themename='darkly')

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

pw1=ttk.Panedwindow(app, orient=HORIZONTAL, bootstyle=PRIMARY)
pw1.grid(row=0, column=0, sticky=N+S+W+E)
left = ttk.Label(pw1, text="left pane")
pw1.add(left)

pw2 = ttk.PanedWindow(pw1, orient=VERTICAL, bootstyle=PRIMARY)
pw1.add(pw2)

top = ttk.Label(pw2, text="top pane")
pw2.add(top)

bottom = ttk.Label(pw2, text="bottom pane")
pw2.add(bottom)

app.mainloop()



