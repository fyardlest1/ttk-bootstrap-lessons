import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title='Text Entry Styles', themename='darkly')

# Place lebels and text entry elements
leb1 = ttk.Label(app, text='Text Entry 1', bootstyle=SUCCESS)
leb1.grid(row=0, column=0, sticky=N+S+E+W)

te1 = ttk.Entry(app, bootstyle=SUCCESS)
te1.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+E+W)

# Second Set
leb2 = ttk.Label(app, text='Text Entry 1', bootstyle=SUCCESS)
leb2.grid(row=1, column=0, sticky=N+S+E+W)

te2 = ttk.Entry(app, bootstyle=SUCCESS)
te2.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+E+W)

# Start the UI
app.mainloop()