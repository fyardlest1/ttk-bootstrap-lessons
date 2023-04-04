import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title="Scale Styles", themename="darkly")

# manually update the gauge value
s1 = ttk.Scale(app,from_ = 1, to = 100, orient=HORIZONTAL, bootstyle=PRIMARY)
s1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)

s2 = ttk.Scale(app,from_ = 1, to = 100, orient=HORIZONTAL,bootstyle=SUCCESS)
s2.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+W+E)
s2.configure(value=50)

s3 = ttk.Scale(app,from_ = 1, to = 100, orient=HORIZONTAL, bootstyle=INFO)
s3.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+W+E)

s4 = ttk.Scale(app,from_ = 1, to = 100, orient=HORIZONTAL,bootstyle=DANGER)
s4.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+W+E)
s4.configure(value=75)

# Start the UI
app.mainloop()


