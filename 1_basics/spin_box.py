import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
root = ttk.Window(title='Spinbox Styles', themename='darkly')

# Place spinbox in the window
sb1_value = ttk.StringVar(value=0)
sb1 = ttk.Spinbox(root, from_=0, to=30, textvariable=sb1_value, wrap=True, bootstyle=SUCCESS)
sb1.grid(row=0, column=0, padx=5, pady=5, sticky=(N+S+E+W))

# Start the UI
root.mainloop()