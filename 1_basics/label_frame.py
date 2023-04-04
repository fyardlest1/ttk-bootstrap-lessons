import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title='Labelframes Styles', themename='darkly')

#  First one
lf1 = ttk.LabelFrame(app, text='This is a LabelFrame', bootstyle=DEFAULT)
lf1.grid(row=0, column=0, padx=5, pady=5, sticky=(N+S+E+W))

lb1 = ttk.Label(lf1, text='Primary Style LabelFrame')
lb1.grid(row=0, column=0, padx=5, pady=5, sticky=(N+S+E+W))

# Second
lf2 = ttk.LabelFrame(app, text='Information Style LabelFrame', bootstyle=INFO)
lf2.grid(row=0, column=1, padx=5, pady=5, sticky=(N+S+E+W))

lb2 = ttk.Label(lf2, text='INFO Style LabelFrame')
lb2.grid(row=0, column=0, padx=5, pady=5, sticky=(N+S+E+W))


# Start the UI
app.mainloop()