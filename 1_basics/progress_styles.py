import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title="Progress Bar Styles", themename="darkly")

# Setup the bars
pb1 = ttk.Progressbar(app, value=25, orient=HORIZONTAL, bootstyle=INFO)
pb1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)
pb1.configure(value=25)

pb2 = ttk.Progressbar(app, orient=HORIZONTAL, bootstyle=WARNING)
pb2.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+W+E)
pb2.configure(value=75)

pb3 = ttk.Progressbar(app, orient=HORIZONTAL, bootstyle="INFO-STRIPED")
pb3.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+W+E)
pb3.configure(value=75)

pb4 = ttk.Progressbar(app, orient=HORIZONTAL, bootstyle="WARNING-STRIPED")
pb4.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+W+E)
pb4.configure(value=75)

# Start the UI
app.mainloop()


