import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
root = ttk.Window(title="Checkbutton Styles", themename="darkly")

# Place a series of demo buttons in the window
b1 = ttk.Checkbutton(root, text="Round Toggle", bootstyle="round-toggle")
b1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)

b2 = ttk.Checkbutton(root, text="Info Round Toggle", bootstyle="info-round-toggle")
b2.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+W+E)

b3 = ttk.Checkbutton(root, text="Square Toggle", bootstyle="square-toggle")
b3.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+W+E)

b4 = ttk.Checkbutton(root, text="Info Square Toggle", bootstyle="info-square-toggle")
b4.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+W+E)

# Start the UI
root.mainloop()


