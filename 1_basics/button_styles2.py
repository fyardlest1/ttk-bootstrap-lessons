import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
root = ttk.Window(title="Button Styles", themename="darkly")

# Place a series of demo buttons in the window
b1 = ttk.Button(root, text="Default", bootstyle="OUTLINE-DEFAULT")
b1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)

b2 = ttk.Button(root, text="Success", bootstyle="OUTLINE-SUCCESS")
b2.grid(row=0, column=3, padx=5, pady=5, sticky=N+S+W+E)

b3 = ttk.Button(root, text="Info", bootstyle="OUTLINE-INFO")
b3.grid(row=0, column=4, padx=5, pady=5, sticky=N+S+W+E)

b4 = ttk.Button(root, text="Warning", bootstyle="OUTLINE-WARNING")
b4.grid(row=0, column=5, padx=5, pady=5, sticky=N+S+W+E)

# Start the UI
root.mainloop()

