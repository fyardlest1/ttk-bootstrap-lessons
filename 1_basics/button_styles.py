import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
root = ttk.Window(title="Button Styles", themename="darkly")

# Place a series of demo buttons in the window
b1 = ttk.Button(root, text="Default", bootstyle=DEFAULT)
b1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)

b2 = ttk.Button(root, text="Primary", bootstyle=PRIMARY)
b2.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+W+E)

b3 = ttk.Button(root, text="Secondary", bootstyle=SECONDARY)
b3.grid(row=0, column=2, padx=5, pady=5, sticky=N+S+W+E)

b4 = ttk.Button(root, text="Success", bootstyle=SUCCESS)
b4.grid(row=0, column=3, padx=5, pady=5, sticky=N+S+W+E)

b5 = ttk.Button(root, text="Info", bootstyle=INFO)
b5.grid(row=0, column=4, padx=5, pady=5, sticky=N+S+W+E)

b6 = ttk.Button(root, text="Warning", bootstyle=WARNING)
b6.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+W+E)

b7 = ttk.Button(root, text="Danger", bootstyle=DANGER)
b7.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+W+E)

b8 = ttk.Button(root, text="Light", bootstyle=LIGHT)
b8.grid(row=1, column=2, padx=5, pady=5, sticky=N+S+W+E)

b9 = ttk.Button(root, text="Dark", bootstyle=DARK)
b9.grid(row=1, column=3, padx=5, pady=5, sticky=N+S+W+E)

b10 = ttk.Button(root, text="Disabled", bootstyle=DISABLED)
b10.grid(row=1, column=4, padx=5, pady=5, sticky=N+S+W+E)


# Start the UI
root.mainloop()