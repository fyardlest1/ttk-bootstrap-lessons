import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title="Radiobutton Styles", themename="darkly")

# Place a series of demo buttons in the window
b1 = ttk.Radiobutton(app, text="Default", bootstyle=DEFAULT)
b1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)

b2 = ttk.Radiobutton(app, text="Primary", bootstyle=PRIMARY)
b2.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+W+E)

b3 = ttk.Radiobutton(app, text="Secondary", bootstyle=SECONDARY)
b3.grid(row=0, column=2, padx=5, pady=5, sticky=N+S+W+E)

b4 = ttk.Radiobutton(app, text="Success", bootstyle=SUCCESS)
b4.grid(row=0, column=3, padx=5, pady=5, sticky=N+S+W+E)

b5 = ttk.Radiobutton(app, text="Info", bootstyle=INFO)
b5.grid(row=0, column=4, padx=5, pady=5, sticky=N+S+W+E)

b6 = ttk.Radiobutton(app, text="Warning", bootstyle=WARNING)
b6.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+W+E)

b7 = ttk.Radiobutton(app, text="Danger", bootstyle=DANGER)
b7.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+W+E)

b8 = ttk.Radiobutton(app, text="Light", bootstyle=LIGHT)
b8.grid(row=1, column=2, padx=5, pady=5, sticky=N+S+W+E)

b9 = ttk.Radiobutton(app, text="Dark", bootstyle=DARK)
b9.grid(row=1, column=3, padx=5, pady=5, sticky=N+S+W+E)

b10 = ttk.Radiobutton(app, text="Disabled", bootstyle=DISABLED)
b10.grid(row=1, column=4, padx=5, pady=5, sticky=N+S+W+E)

# Start the UI
app.mainloop()


