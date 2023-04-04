import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title='Menu Button Styles', themename='darkly')

#  Place a series of demo meters in the windows
me1 = ttk.Meter(app, metersize=100, amountused=25, bootstyle=DEFAULT)
me1.grid(row=0, column=0, padx=5, pady=5, sticky=(N+S+E+W))

me2 = ttk.Meter(app, metersize=100, amountused=50, bootstyle=SUCCESS)
me2.grid(row=0, column=1, padx=5, pady=5, sticky=(N+S+E+W))

me3 = ttk.Meter(app, metersize=100, amountused=75, bootstyle=INFO)
me3.grid(row=0, column=2, padx=5, pady=5, sticky=(N+S+E+W))

me4 = ttk.Meter(app, metersize=100, amountused=95, bootstyle=WARNING)
me4.grid(row=0, column=3, padx=5, pady=5, sticky=(N+S+E+W))

me5 = ttk.Meter(app, metersize=100, amountused=35, bootstyle=DANGER)
me5.grid(row=1, column=0, padx=5, pady=5, sticky=(N+S+E+W))

me6 = ttk.Meter(app, metersize=100, amountused=65, bootstyle=WARNING)
me6.grid(row=1, column=1, padx=5, pady=5, sticky=(N+S+E+W))

me7 = ttk.Meter(app, metersize=100, amountused=85, bootstyle=LIGHT)
me7.grid(row=1, column=2, padx=5, pady=5, sticky=(N+S+E+W))

me8 = ttk.Meter(app, metersize=100, amountused=100, bootstyle=DISABLED)
me8.grid(row=1, column=3, padx=5, pady=5, sticky=(N+S+E+W))


# Start the UI
app.mainloop()