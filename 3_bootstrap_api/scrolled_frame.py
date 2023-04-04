import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

app = ttk.Window()

sf = ScrolledFrame(app, autohide=True)
sf.grid(row=0, column=0, padx=5, pady=5, sticky=(N+S+E+W))

# add a number of checkbuttons into the scrolled frame
for x in range(10):
    ttk.Checkbutton(sf, text=f"Checkbutton {x}").grid(row=x, column=0, sticky=(N+S+E+W))

app.mainloop()

