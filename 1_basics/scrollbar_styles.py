import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title="Scrollbar Styles", themename="darkly")

# Horizontal (x) Scroll bar
xsb = ttk.Scrollbar(app, orient=HORIZONTAL, bootstyle=DEFAULT)
xsb.grid(row=1, column=0, sticky=N+S+W+E)

# Vertical (y) Scroll Bar
ysb = ttk.Scrollbar(app, orient=VERTICAL, bootstyle=DEFAULT)
ysb.grid(row=0,column=1, sticky=N+S+W+E)

# Text Widget
t1 = ttk.Text(app, wrap=NONE, xscrollcommand=xsb.set, yscrollcommand=ysb.set)
t1.grid(row=0, column=0)

# Configure the scrollbars
xsb.config(command=t1.xview)
ysb.config(command=t1.yview)

# Run tkinter main loop
app.mainloop()