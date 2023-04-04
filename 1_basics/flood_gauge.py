import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title='Floodgauge Styles', themename='cosmo')

# Place lebels and text entry elements
fg1 = ttk.Floodgauge(app, orient=VERTICAL, bootstyle=DEFAULT)
fg1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+E+W)

# Start autoincrement, set step by 10, end autoincrement
fg1.start()
fg1.step(10)
fg1.stop()

# Manually update the gauge value
fg2 = ttk.Floodgauge(app, text='25%', orient=VERTICAL, bootstyle=INFO)
fg2.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+E+W)
fg2.configure(value=25)

fg3 = ttk.Floodgauge(app, text='75%', orient=VERTICAL, bootstyle=WARNING)
fg3.grid(row=0, column=2, padx=5, pady=5, sticky=N+S+E+W)
fg3.configure(value=75)



# Start the UI
app.mainloop()