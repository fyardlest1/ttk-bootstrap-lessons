import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
root = ttk.Window(title='Date Entry Style', themename='darkly')

# Place a date entry in the window
de1 = ttk.DateEntry(root, bootstyle=PRIMARY)
de1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+S+W)


# Start the UI
root.mainloop()